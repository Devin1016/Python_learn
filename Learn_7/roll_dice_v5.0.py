'''
    功能：模拟抛掷1个骰子，并输出结果
    版本:V5.0
    V2.0新增功能：模拟投掷2个骰子
    V3.0新增功能：可视化投掷2个骰子的结果
    V4.0新增功能：对结果进行简单的数据统计和分析
    V5.0新增功能：使用科学计算库简化程序，完善数据可视化结果
'''

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    total_times = 10000

    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)

    result_arr = roll1_arr + roll2_arr + roll3_arr

    hist, bins = np.histogram(result_arr, bins=range(3, 19))
    print(result_arr)
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(
        result_arr,
        bins=range(3, 20),
        normed=1,
        edgecolor='black',
        linewidth=0.5,
        rwidth=0.8)

    # 设置x轴坐标点显示
    tick_labels = [
        '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点', '13点',
        '14点', '15点', '16点', '17点', '18点'
    ]
    tick_pos = np.arange(3, 19) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
