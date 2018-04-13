# 汇率换算器——3

# 设置汇率
usd_vs_rmb = 6.77

# 获取输入字符串
currency_str_value = input("请输入代单位的货币金额（退出程序请输入Q）：")

i = 0

# 判断用户是否退出
while currency_str_value != 'Q':
    i += 1
    print("第", i, "次计算")
    # 获取货币种类
    unit = currency_str_value[-3:]

    # 判断货币种类并计算
    # 输入的是人民币
    if unit == 'CNY':
        # 获取人民币数量str
        rmb_str_value = currency_str_value[:-3]
        # 包含数字的str转换为number
        rmb_value = eval(rmb_str_value)
        # 汇率计算
        value = rmb_value / usd_vs_rmb
        # 输出换算金额
        print('换算后金额为：', value, "USD")
    # 输入的是美元
    elif unit == 'USD':
        # 获取美元数量str
        usd_str_value = currency_str_value[:-3]
        # 包含数字的str转换为number
        usd_value = eval(usd_str_value)
        # 汇率计算
        value = usd_value * usd_vs_rmb
        # 输出换算金额
        print('换算后金额为：', value, "CNY")
    # 输入的是其他货币
    else:
        print('不支持该币种换算。')
    print('*****************************************************')
    # 获取输入字符串
    currency_str_value = input("请输入代单位的货币金额（退出程序请输入Q）：")
# 成功退出程序
print('程序已退出。')
