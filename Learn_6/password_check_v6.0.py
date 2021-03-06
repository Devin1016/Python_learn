'''
    功能：检查密码强度
        1、密码长度至少8位
        2、密码含有数字
        3、密码含有字母
    版本:V6.0
    V2.0增加功能：限制设置密码次数，终止循环
    V3.0增加功能：保存设置的密码及其对应的强度到文件中
    V4.0增加功能：读取文件中的密码
    V5.0增加功能：定义一个password的工具类
    V6.0增加功能：定义一个文件操作的工具类
'''


# 文件工具类
class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_to_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


# 密码工具类
class PasswordTool:
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    # 类的方法
    # 检测密码强度
    def process_password(self):
        # 密码长度
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少为8位。')

        # 包含数字
        if self.check_number():
            self.strength_level += 1
        else:
            print('密码需要包含数字。')

        # 包含字母
        if self.check_letter():
            self.strength_level += 1
        else:
            print('密码需要包含字母。')

    # 判断是否包含数字
    def check_number(self):
        has_number = False

        for x in self.password:
            if x.isnumeric():
                has_number = True
                break

        return has_number

    # 判断是否包含字母
    def check_letter(self):
        has_letter = False

        for x in self.password:
            if x.isalpha():
                has_letter = True
                break

        return has_letter


def main():
    try_times = 0

    # 实例化文件操作类
    file_tool = FileTool('./Learn_6/password.cfg')

    while try_times < 5:
        password = input('请输入密码：\n1、密码长度至少8位;2、密码含有数字;3、密码含有字母。\n')

        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        if password_tool.strength_level == 1:
            strength = '弱'
        elif password_tool.strength_level == 2:
            strength = '较弱'
        else:
            strength = '强'

        # 写文件
        file_tool.write_to_file('密码：{}，强度：{}\n'.format(password, strength))

        if password_tool.strength_level == 3:
            print('密码强度合格。')
            break
        else:
            print('密码强度不够。')
            try_times += 1

    if try_times >= 5:
        print('尝试次数过多，密码设置失败。')

    # 读操作
    lines = file_tool.read_to_file()
    print(lines)


if __name__ == '__main__':
    main()
