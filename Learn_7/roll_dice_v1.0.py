'''
    功能：模拟抛掷1个骰子，并输出结果
    版本:V1.0
'''

import random


# 模拟掷骰子
def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    # 初始化记录列表
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j - 1] += 1

    for i, result in enumerate(result_list):
        print('点数{}的次数：{}，频率：{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
