class bmr:
    def bmr(bmr_str):
        str_list = bmr_str.split(' ')
        gender = str_list[0]
        try:
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])

            if gender == '男':
                # 男性BMR
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            elif gender == '女':
                # 女性BMR
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 665
            else:
                bmr = -1

            if bmr != -1:
                print('您的性别：{}，体重：{}kg，身高：{}cm，年龄：{}'.format(
                    gender, weight, height, age))
                print('您的基础代谢率BMR：{}大卡'.format(bmr))
            else:
                print('暂不支持该计算！')
        except ValueError:
            print('请按正确格式输入信息！')
        except IndexError:
            print('你输入的信息缺失！')
        except Exception:
            print('程序异常，请重试！')

    def bmr_final():
        # 主函数
        qt = input('是否退出程序（y/n）？')

        while qt != 'y':
            print('请输入以下信息，用空格分割')
            input_str = input('性别 体重（kg） 身高（cm） 年龄：')
            bmr(input_str)
            qt = input('是否退出程序（y/n）？')
