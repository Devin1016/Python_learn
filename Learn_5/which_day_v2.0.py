'''
    功能：判断是一年中的第几天
    版本：V2.0
    V2.0新增功能：使用列表替换元组
'''

from datetime import datetime


def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    input_date_str = input('请输入日期（YYYY/MM/DD）：')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month_list[1] = 29

    days = sum(days_in_month_list[:month - 1]) + day

    print('这是{}的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
