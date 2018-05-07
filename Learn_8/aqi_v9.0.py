'''
    功能：AQI计算
    版本：V9.0
    V2.0新增功能：读取json数据，并输出数据到json文件
    V3.0新增功能：读取json数据，并输出数据到csv文件
    V4.0新增功能：判断文件为json还是csv，并进行相应操作
    V5.0新增功能：网络爬虫，实时获取aqi网络数据
    V6.0新增功能：使用beatifulsoup4解析网页
    V7.0新增功能：获取所有城市的aqi
    V8.0新增功能：将获取城市aqi保存为csv文件
    V9.0新增功能：将获取数据进行分析
'''

import pandas as pd


def main():
    aqi_data = pd.read_csv('.\Learn_8\china_city_aqi.csv')

    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 基本统计
    print('AQI最大值:', aqi_data['AQI'].max())
    print('AQI最小值:', aqi_data['AQI'].min())
    print('AQI平均值:', aqi_data['AQI'].mean())

    # top10城市
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # bottom10
    bottom10_cities = aqi_data.sort_values(
        by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('.\Learn_8\china_top10_city_aqi.csv', index=False)
    bottom10_cities.to_csv(
        '.\Learn_8\china_bottom10_city_aqi.csv', index=False)


if __name__ == '__main__':
    main()
