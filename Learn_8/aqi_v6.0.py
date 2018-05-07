'''
    功能：AQI计算
    版本：V6.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
    V4.0新增功能：判断文件为json还是csv，并进行相应操作
    V5.0新增功能：网络爬虫，实时获取aqi网络数据
    V6.0新增功能：使用beatifulsoup4解析网页
'''

import requests
from bs4 import BeautifulSoup


# 获取城市aqi
def get_city_text(city_py):
    url = 'http://pm25.in/' + city_py
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []

    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))

    return city_aqi


def main():
    city_py = input('请输入城市拼音：')
    city_api = get_city_text(city_py)

    print('空气质量指数为：{}'.format(city_api))


if __name__ == '__main__':
    main()
