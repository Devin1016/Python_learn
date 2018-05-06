class currency:
    # 主函数
    def con_currreny():
        # 设置汇率
        usd_vs_rmb = 6.77

        # 获取输入字符串
        currency_str_value = input("请输入代单位的货币金额：")

        in_money = eval(currency_str_value[:-3])

        unit = currency_str_value[-3:]

        # 输入的是人民币
        if unit == 'CNY':
            exchange_rate = 1 / usd_vs_rmb
            print('换算后的金额：{}{}'.format(in_money * exchange_rate, 'USD'))
        # 输入的是美元
        elif unit == 'USD':
            exchange_rate = usd_vs_rmb
            print('换算后的金额：{}{}'.format(in_money * exchange_rate, 'CNY'))
        # 输入的是其他货币
        else:
            print('不支持该货币换算。')
