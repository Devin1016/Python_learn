'''
    功能：AQI计算
    版本：V3.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
'''

import json
import csv


# 解析json文件
def process_json_file(filepath):
    f = open(filepath, 'r', encoding='UTF-8')
    city_list = json.load(f)
    return city_list


def main():
    area_num = int(input('请选择地区：\n1、北京；2、上海。\n'))

    if area_num == 1:
        file_path = './Learn_8/beijing_aqi.json'
    elif area_num == 2:
        file_path = './Learn_8/shanghai_aqi.json'
    else:
        print('你选择的地区不存在')

    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])

    lines_list = []
    # 获取列名
    lines_list.append(list(city_list[0].keys()))
    # 获取对应数据
    for city in city_list:
        lines_list.append(list(city.values()))

    f = open('./Learn_8/aqi.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines_list:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
