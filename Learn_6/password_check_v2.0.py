'''
    功能：检查密码强度
        1、密码长度至少8位
        2、密码含有数字
        3、密码含有字母
    版本:V2.0
    V2.0增加
    功能：限制设置密码次数，终止循环
'''


# 判断是否包含数字
def check_number(password_str):
    has_number = False

    for x in password_str:
        if x.isnumeric():
            has_number = True
            break

    return has_number


# 判断是否包含字母
def check_letter(password_str):
    has_letter = False

    for x in password_str:
        if x.isalpha():
            has_letter = True
            break

    return has_letter


def main():
    try_times = 0

    while try_times < 5:
        password = input('请输入密码：\n1、密码长度至少8位;2、密码含有数字;3、密码含有字母。\n')

        strength_level = 0

        # 密码长度
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度至少为8位。')
            try_times += 1

        # 包含数字
        if check_number(password):
            strength_level += 1
        else:
            print('密码需要包含数字。')
            try_times += 1

        # 包含字母
        if check_letter(password):
            strength_level += 1
        else:
            print('密码需要包含字母。')
            try_times += 1

        if strength_level == 3:
            print('密码强度合格。')
            break
        else:
            print('密码强度不够。')
            try_times += 1

    if try_times >= 5:
        print('尝试次数过多，密码设置失败。')


if __name__ == '__main__':
    main()
