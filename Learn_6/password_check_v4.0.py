'''
    功能：检查密码强度
        1、密码长度至少8位
        2、密码含有数字
        3、密码含有字母
    版本:V4.0
    V2.0增加功能：限制设置密码次数，终止循环
    V3.0增加功能：保存设置的密码及其对应的强度到文件中
    V4.0增加功能：读取文件中的密码
'''


def main():
    f = open('./Learn_6/password.cfg', 'r')

    # content = f.read()

    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    for line in f:
        print('read:{}'.format(line))

    f.close()


if __name__ == '__main__':
    main()
