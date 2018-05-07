'''
    功能：模拟抛掷1个骰子，并输出结果
    版本:V4.0
    V2.0新增功能：模拟投掷2个骰子
    V3.0新增功能：可视化投掷2个骰子的结果
    V4.0新增功能：对结果进行简单的数据统计和分析
'''

import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 模拟掷骰子
def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000

    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    # 数据可视化
    plt.hist(
        roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
