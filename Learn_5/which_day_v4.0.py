'''
    功能：判断是一年中的第几天
    版本：V4.0
    V2.0新增功能：使用列表替换元组
    V3.0新增功能：将月份划分不同集合
    V4.0新增功能：将月份和天数使用字典表示
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

    # 月份的字典
    month_day_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    day_month_dict = {
        30: {4, 6, 9, 11},
        31: {1, 3, 5, 7, 8, 10, 12}
    }

    days = day
    days_1 = day

    for i in range(1, month):
        if i in day_month_dict[30]:
            days_1 += 30
        elif i in day_month_dict[31]:
            days_1 += 31
        else:
            days_1 += 28

    for i in range(1, month):
        days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1
        days_1 += 1

    print('这是{}的第{}天。'.format(year, days))
    print('这是{}的第{}天。'.format(year, days_1))


if __name__ == '__main__':
    main()
