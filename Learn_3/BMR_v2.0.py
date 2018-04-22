"""
    功能：BMR计算器
    版本：2.0
    V2.0:根据用户输入计算BMR，直到用户退出
"""


def main():
    # 主函数
    exit = input('是否退出程序（y/n）？')

    while exit != 'y':
        # 性别
        gender = input('性别（男/女）：')

        # 体重
        weight = float(input('体重（kg）：'))

        # 身高
        height = float(input('身高（cm）：'))

        # 年龄
        age = int(input('年龄：'))

        if gender == '男':
            # 男性BMR
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性BMR
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 665
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率BMR（大卡）：', bmr)
        else:
            print('暂不支持该计算！')

        print()
        exit = input('是否退出程序（y/n）？')


if __name__ == '__main__':
    main()
