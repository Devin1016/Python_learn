# 汇率换算器——5


def convert_currency(im, er):
    out = im * er
    return out


# 主函数
def main():
    # 设置汇率
    usd_vs_rmb = 6.77

    # 获取输入字符串
    currency_str_value = input("请输入代单位的货币金额：")

    unit = currency_str_value[-3:]

    # 输入的是人民币
    if unit == 'CNY':
        exchange_rate = 1 / usd_vs_rmb
    # 输入的是美元
    elif unit == 'USD':
        exchange_rate = usd_vs_rmb
    # 输入的是其他货币
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        # convert_currency2 = lambda x: x * exchange_rate
        def convert_currency2(x): return x * exchange_rate
        in_money = eval(currency_str_value[:-3])
        out_money = convert_currency(in_money, exchange_rate)
        out_money2 = convert_currency2(in_money)
        print('换算后的金额：', out_money)
        print('换算后的金额：', out_money2)
    else:
        print('不支持该货币换算。')


if __name__ == '__main__':
    main()
