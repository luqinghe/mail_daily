import requests


def get_info():
    '''获取天气信息'''
    weather_url = 'http://t.weather.sojson.com/api/weather/city/101010200'

    # 取api数据
    r = requests.get(weather_url)
    # 解析
    weather = r.json()

    # 锁定今天
    today = weather['data']['forecast'][0]
    # # 高温 13.0℃
    # today['high']
    # # 低温 -2.0℃
    # today['low']
    # # 空气质量
    # weather['data']['quality']
    # # 风向
    # today['fx']
    # # 风力等级
    # today['fl']
    # # 晴
    # today['type']
    # # 提示
    # today['notice']

    today_weather = '天气：%s，空气质量：%s，%s，%s，%s' % (
        today['type'], weather['data']['quality'], today['high'], today['low'], today['fx']+today['fl'])
    today_notice = today['notice']
    # 明日
    tomorrow = weather['data']['forecast'][1]
    tomorrow_weather = '天气：%s，%s，%s，%s' % (
        tomorrow['type'], tomorrow['high'], tomorrow['low'], tomorrow['fx']+tomorrow['fl'])
    tomorrow_notice = tomorrow['notice']

    return (today_weather, today_notice, tomorrow_weather, tomorrow_notice)
