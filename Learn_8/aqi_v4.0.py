'''
    功能：AQI计算
    版本：V4.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
    V4.0新增功能：判断文件为json还是csv，并进行相应操作
'''

import json
import csv
import os


# 解析json文件
def process_json_file(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        city_list = json.load(f)
    print(city_list)


# 解析csv文件
def process_csv_file(filepath):
    with open(filepath, 'r', encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    file_path = input('请输入文件名称：')
    fliename, file_ext = os.path.splitext(file_path)

    # 判断文件类型
    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('这是不支持的文件格式。')


if __name__ == '__main__':
    main()
