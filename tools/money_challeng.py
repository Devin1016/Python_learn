import math
import datetime


class money:
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

    def money_challeng():
        # 每周存入金额
        money_per_week = float(input('请输入每周存入金额：'))
        # 递增的金额
        increase_money = float(input('请输入每周递增金额：'))
        # 总周数
        total_week = int(input('请输入存款周数：'))

        saved_money_list = money.save_money_in_n_weeks(
            money_per_week, increase_money, total_week)

        # 输入日期
        input_date_str = input('请输入日期（yyyy/mm/dd）:')

        # 转换str为datetime格式
        input_date = datetime.datetime.strptime(input_date_str,
                                                format('%Y/%m/%d'))

        # 用户输入第几周
        week_num = input_date.isocalendar()[1]

        print('第{}周的存款为：{}元'.format(week_num, saved_money_list[week_num - 1]))
