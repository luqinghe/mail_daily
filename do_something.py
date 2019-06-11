import datetime
import time
import one
import weather
import my_email
from string import Template


def _get_html():
    '''根据模板生成html'''

     # 获取照片及one_world
    one_word = one.get_info()

    # 获取天气信息
    weather_info = weather.get_info()
    today_weather = weather_info[0]
    today_notice = weather_info[1]
    tomorrow_weather = weather_info[2]
    tomorrow_notice = weather_info[3]

    # 今明两天日期
    today = datetime.date.today()
    today_date = today.strftime('%Y-%m-%d')
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_date = tomorrow.strftime('%Y-%m-%d')

    # 读取模板
    f = open('template.html', 'r', encoding='UTF-8')
    template = f.read()
    html_template = Template(template)
    html = html_template.safe_substitute(today_date=today_date, tomorrow_date=tomorrow_date,
                                         today_weather=today_weather, today_notice=today_notice,
                                         tomorrow_weather=tomorrow_weather, tomorrow_notice=tomorrow_notice,
                                         one_word=one_word)
    f.close()

    return html

def _get_address():
    '''读取发件人和收件人地址'''
    addrs = []
    with open('addrs.txt', 'r', encoding='UTF_8') as f:
        for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            addr_info = line.split(',')
            addrs.append((addr_info[0], addr_info[1]))
    # 第一行是发件人
    from_addr = addrs[0]
    # 后面的是收件人
    to_addr = addrs[1:]
    return from_addr, to_addr

def do():
    '''执行定时任务'''

    # 根据模板生成html
    html = _get_html()

    from_addr, to_addr = _get_address()
    # 发送邮件
    # my_email.send_emails(html, from_addr, to_addr)
    my_email.send_separated_emails(html, from_addr, to_addr)


def main(h=8, m=0):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如8:00
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
                break
            # 每20秒检测一次
            time.sleep(20)
        print('开始执行任务。。。')
        try:
            do()
        except:
            print("发送失败，失败时间%s。" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                        
        # 跳过这分钟
        time.sleep(60)


if __name__ == "__main__":
    main()
    # do()
