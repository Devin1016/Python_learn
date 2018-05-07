'''
    功能：模拟抛掷1个骰子，并输出结果
    版本:V3.0
    V2.0新增功能：模拟投掷2个骰子
    V3.0新增功能：可视化投掷2个骰子的结果
'''

import random
import matplotlib.pyplot as plt


# 模拟掷骰子
def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 1000
    # 初始化结果列表
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    result_dict = dict(zip(roll_list, result_list))

    # 记录一个骰子结果
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        roll = roll1 + roll2
        for j in range(2, 13):
            if roll == j:
                result_dict[j] += 1

    for i, result in result_dict.items():
        print('点数{}的次数：{}，频率：{}'.format(i, result, result / total_times))

    # 数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, alpha=0.5, c="red")
    plt.scatter(x, roll2_list, alpha=0.5, c='green')
    plt.show()


if __name__ == '__main__':
    main()
