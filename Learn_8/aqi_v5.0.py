'''
    功能：AQI计算
    版本：V5.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
    V4.0新增功能：判断文件为json还是csv，并进行相应操作
    V5.0新增功能：网络爬虫，实时获取aqi网络数据
'''

import requests


# 返回url的文本
def get_html_text(url):
    r = requests.get(url, timeout=30)
    return r.text


def main():
    city_py = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_py

    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''

    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3

    aqi_val = url_text[begin_index: end_index]

    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
