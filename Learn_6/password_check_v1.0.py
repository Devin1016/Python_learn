'''
    功能：检查密码强度
        1、密码长度至少8位
        2、密码含有数字
        3、密码含有字母
    版本:V1.0
'''


def check_number(password_str):
    exist = False
    for x in password_str:
        if x.isnumeric():
            exist = True
            break
    return exist


def check_letter(password_str):
    exist = False
    for x in password_str:
        if x.isalpha():
            exist = True
            break
    return exist


def main():
    password = input('请输入密码：\n1、密码长度至少8位;2、密码含有数字;3、密码含有字母。\n')
    strength_level = 0

    # 密码长度
    if len(password) >= 8:
        strength_level += 1
    else:
        print('密码长度至少为8位。')

    # 包含数字
    if check_number(password):
        strength_level += 1
    else:
        print('密码需要包含数字。')

    # 包含字母
    if check_letter(password):
        strength_level += 1
    else:
        print('密码需要包含字母。')

    if strength_level == 3:
        print('密码强度合格。')
    else:
        print('密码强度不够。')


if __name__ == '__main__':
    main()
