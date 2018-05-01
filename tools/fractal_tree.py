"""
    功能：利用递归绘制分形树
    版本：1.0
"""

import turtle


class fractal:
    # 树枝绘制函数
    def draw_branch(branch_length):
        if branch_length > 5:
            # 绘制右侧树枝
            turtle.forward(branch_length)
            print('向前：', branch_length)
            turtle.right(20)
            print('右转20度')
            fractal.draw_branch(branch_length - 20)

            # 绘制左侧树枝
            turtle.left(40)
            print('左转40度')
            fractal.draw_branch(branch_length - 20)

            # 返回之前的树枝
            turtle.right(20)
            print('右转20度')
            turtle.backward(branch_length)
            print('退后：', branch_length)

        if branch_length < 40:
            turtle.pencolor('green')
        else:
            turtle.color('brown')

    # 主函数
    def fractal():
        turtle.color('brown')
        turtle.pensize(3)
        turtle.left(90)
        turtle.penup()
        turtle.backward(100)
        turtle.pendown()
        fractal.draw_branch(50)
        turtle.exitonclick()
