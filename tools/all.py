'''
    功能组合
'''

from BMR_final import bmr
from currency_converter import currency
from fractal_tree import fractal
from money_challeng import money


def main():
    tools = int(input('工具列表：\n1.汇率计算器\n2.分形树\n3.BMR计算器\n4.存钱计算器\n请选择使用工具：'))
    if tools == 1:
        currency.con_currreny()
    elif tools == 2:
        fractal.fractal()
    elif tools == 3:
        bmr.bmr_final()
    elif tools == 4:
        money.money_challeng()
    else:
        print('不存在你选择的工具。')


if __name__ == '__main__':
    main()
