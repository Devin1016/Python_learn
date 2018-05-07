'''
    功能：AQI计算
    版本：V10.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
    V4.0新增功能：判断文件为json还是csv，并进行相应操作
    V5.0新增功能：网络爬虫，实时获取aqi网络数据
    V6.0新增功能：使用beatifulsoup4解析网页
    V7.0新增功能：获取所有城市的aqi
    V8.0新增功能：将获取城市aqi保存为csv文件
    V9.0新增功能：将获取数据进行分析
    V10.0新增功能：数据清洗，数据可视化
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('.\Learn_8\china_city_aqi.csv')

    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 数据清洗 只保留AQI大于0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值:', clean_aqi_data['AQI'].max())
    print('AQI最小值:', clean_aqi_data['AQI'].min())
    print('AQI平均值:', clean_aqi_data['AQI'].mean())

    # top50城市
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(
        kind='bar', x='City', y='AQI', title='空气质量最好的50个城市', figsize=(20, 10))
    plt.savefig('./Learn_8/top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
