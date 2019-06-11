import smtplib
import configparser
import datetime
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr


def _formataddr(name, addr):
    return formataddr((Header(name, 'utf-8').encode(), addr))


def _biuld_msg(html, from_addr=None, to_addrs=None):
    '''构建邮件对象\n
    from_addr : (name, address)\n
    to_addrs : [(name1, address1), (name2, address2),]
    '''
    msg = MIMEMultipart('image', 'png')
    if from_addr:
        msg['From'] = _formataddr(from_addr[0], from_addr[1])
    if to_addrs:
        to = [_formataddr(name, address) for name, address in to_addrs]
        msg['To'] = ','.join(to)

    msg['Subject'] = Header('一封暖暖的小邮件......', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    # 图片
    image_name = 'one'
    with open('%s.png' % image_name, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment',
                       filename='%s.png' % image_name)
        img.add_header('Content-ID', '<%s>' % image_name)
        img.add_header('X-Attachment-Id', '%s' % image_name)
        msg.attach(img)

    return msg


def _get_server():
    '''连接邮件服务器'''

    # 获取配置信息
    config = configparser.ConfigParser()
    config.read("config.ini")
    smtp_server = config.get('email', 'smtp_server')
    smtp_port = config.get('email', 'smtp_port')
    username = config.get('email', 'username')
    password = config.get('email', 'password')
    # login
    # no ssl
    server = smtplib.SMTP(smtp_server, smtp_port)
    # use ssl
    # server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(username, password)

    return server


def send_emails(html, from_addr, to_addrs):
    '''同时给多个人发送邮件'''

    # 邮件对象
    msg = _biuld_msg(html, from_addr=from_addr, to_addrs=to_addrs)

    server = _get_server()
    server.sendmail(from_addr[1], [address for name, address in to_addrs], msg.as_string())
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('%s已发送至%s' % (nowTime, to_addrs)
    server.quit()


def send_separated_emails(html, from_addr, to_addrs):
    '''多收件人分别发送邮件'''

    server = _get_server()
    # 邮件对象:
    for name, address in to_addrs:
        msg = _biuld_msg(html, from_addr=from_addr)
        msg['To'] = _formataddr(name, address)
        server.sendmail(from_addr[1], [address], msg.as_string())
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s已发送至%s' % (nowTime, to_addrs)
    server.quit()

