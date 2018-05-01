"""
    功能：52周存钱挑战
    版本：4.0
    2.0新增功能：记录每周的存款数
    3.0新增功能：使用循环直接计数
    4.0新增功能：灵活设置每周的存款数，增加的存款数及存款周数
"""

import math


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    # 计算n周的存款金额
    # 账户累计
    saving_money = 0
    # 记录存款数list
    money_list = []

    for i in range(total_week):
        # 记录存钱数
        money_list.append(money_per_week)

        # 存钱操作
        saving_money = math.fsum(money_list)

        # 输出结果
        print("第{}周存入{}元，账户累计为：{}元".format(i+1, money_per_week, saving_money))

        # 更新存钱数据
        money_per_week += increase_money

    return saving_money


def main():
    # 每周存入金额
    money_per_week = float(input('请输入每周存入金额：'))
    # 递增的金额
    increase_money = float(input('请输入每周递增金额：'))
    # 总周数
    total_week = int(input('请输入存款周数：'))

    saving = 0

    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    print(saving)


if __name__ == '__main__':
    main()
