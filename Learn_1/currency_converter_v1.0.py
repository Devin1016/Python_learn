# 汇率换算器——1

# 获取输入字符串
rmb_str_value = input("请输入人民币（CNY）金额：")

# 设置汇率
usd_vs_rmb = 6.77

# 包含数字的str转换为number
rmb_value = eval(rmb_str_value)

# 计算换算后美元
usd_value = rmb_value / usd_vs_rmb

# 输出换算后金额
print("美元（USD）金额：", usd_value)
