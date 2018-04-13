# 汇率换算器——2

# 获取输入字符串
currency_str_value = input("请输入代单位的货币金额：")

# 获取货币种类
unit = currency_str_value[-3:]

# 设置汇率
usd_vs_rmb = 6.77

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
