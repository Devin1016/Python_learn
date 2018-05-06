'''
    功能：判断是一年中的第几天
    版本：V1.0
'''
from datetime import datetime


def main():
    input_date_str = input('请输入日期（YYYY/MM/DD）：')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[:month - 1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days += 1

    print('这是第{}天。'.format(days))


if __name__ == '__main__':
    main()
