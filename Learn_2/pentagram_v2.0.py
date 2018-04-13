"""
    功能：五角星绘制
    版本：2.0
    新增功能：绘制不同大小的五角星
"""

import turtle


# 五角星绘制函数
def draw_pentagram(size):
    # 计数器
    count = 1

    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


# 主函数
def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    while size <= 150:
        # 调用函数绘制
        draw_pentagram(size)
        size += 20

    turtle.exitonclick()


if __name__ == '__main__':
    main()
