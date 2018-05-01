"""
    功能：52周存钱挑战
    版本：5.0
    2.0新增功能：记录每周的存款数
    3.0新增功能：使用循环直接计数
    4.0新增功能：灵活设置每周的存款数，增加的存款数及存款周数
    5.0新增功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
"""

import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    # 计算n周的存款金额
    # 记录存款数list
    money_list = []
    # 记录每周账户累计
    saved_money_list = []

    for i in range(total_week):
        # 记录存钱数
        money_list.append(money_per_week)

        # 存钱操作
        saving_money = math.fsum(money_list)

        # 记录存款累计
        saved_money_list.append(saving_money)

        # 更新存钱数据
        money_per_week += increase_money

    return saved_money_list


def main():
    # 每周存入金额
    money_per_week = float(input('请输入每周存入金额：'))
    # 递增的金额
    increase_money = float(input('请输入每周递增金额：'))
    # 总周数
    total_week = int(input('请输入存款周数：'))

    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money,
                                             total_week)

    # 输入日期
    input_date_str = input('请输入日期（yyyy/mm/dd）:')

    # 转换str为datetime格式
    input_date = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))

    # 用户输入第几周
    week_num = input_date.isocalendar()[1]

    print('第{}周的存款为：{}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()
