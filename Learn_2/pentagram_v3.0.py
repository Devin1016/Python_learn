"""
    功能：五角星绘制
    版本：3.0
    2.0新增功能：绘制不同大小的五角星
    3.0新增功能：使用迭代绘制不同大小的五角星
"""

import turtle


# 五角星绘制函数
def draw_pentagram(size, size_max):
    # 计数器
    count = 1

    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

    if size < size_max:
        size += 20
        draw_pentagram(size, size_max)
    else:
        turtle.exitonclick()


# 主函数
def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    draw_pentagram(50, 150)


if __name__ == '__main__':
    main()
