'''
    功能：模拟抛掷1个骰子，并输出结果
    版本:V2.0
    V2.0新增功能：模拟投掷2个骰子
'''

import random


# 模拟掷骰子
def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    # 初始化结果列表
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    result_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll = roll1 + roll2
        for j in range(2, 13):
            if roll == j:
                result_dict[j] += 1

    for i, result in result_dict.items():
        print('点数{}的次数：{}，频率：{}'.format(i, result, result / total_times))


if __name__ == '__main__':
    main()
