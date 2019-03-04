import requests
import re
from bs4 import BeautifulSoup


def get_info():
    '''获取one的照片和一句话'''
    one_url = 'http://www.wufazhuce.com'

    r = requests.get(one_url)
    html = r.text
    soap = BeautifulSoup(html, "html.parser")

    # 下载图片
    pic_url = soap.find(class_='fp-one-imagen').get('src')
    pic = requests.get(pic_url)
    if pic.status_code == 200:
        with open('one.png', 'wb') as f:
            f.write(pic.content)

    # 图片脚标
    # footer = re.sub(r'\s', '', soap.find(class_='fp-one-imagen-footer').text)
    # print(footer)

    # 每日一句
    one_word = re.sub(r'\s', '', soap.find(class_='fp-one-cita').text)
    print(one_word)

    return one_word
