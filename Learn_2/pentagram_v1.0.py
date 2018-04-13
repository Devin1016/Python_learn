"""
    功能：五角星绘制
    版本：1.0
"""

import turtle


# 主函数
def main():
    # 计数器
    count = 1

    # 绘制五角星
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count += 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
