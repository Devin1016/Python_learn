'''
    功能：AQI计算
    版本：V2.0
    V2.0新增功能：读取json数据，并输出数据到文件
'''

import json


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
    top5_list = city_list[:5]

    f = open('./Learn_8/top5_aqi.json', 'w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()

    print(city_list)


if __name__ == '__main__':
    main()
