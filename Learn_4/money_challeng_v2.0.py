"""
    功能：52周存钱挑战
    版本：2.0
    2.0新增功能：记录每周的存款数
"""

import math


def main():
    # 每周存入金额
    money_per_week = 10
    # 周数
    week = 1
    # 递增的金额
    increase_money = 10
    # 总周数
    total_week = 52
    # 账户累计
    saving_money = 0
    # 记录存款数list
    money_list = []

    while week <= total_week:
        # 记录存钱数
        money_list.append(money_per_week)

        # 存钱操作
        saving_money = math.fsum(money_list)

        # 输出结果
        print("第{}周存入{}元，账户累计为：{}元".format(week, money_per_week, saving_money))

        # 更新存钱数据
        money_per_week += increase_money
        week += 1


if __name__ == '__main__':
    main()
