#国旗宽度A=1.0
#国旗长度B=1.9
#联邦范围宽度：C=0.5385（7/13,7条间纹的阔度）
#联邦范围长度：D=0.76（1.9X2/5，国旗长度的五分之二）
#E=F=0.0538（C/10，联邦范围的十分之一阔度）
#G=H=0.0633(D/12,联邦范围的十二分之一的长度)
#星的直径：K=0.0616
#条纹的宽度：L=0.0769（1/13）
#白色：#FFFFFF
#国旗红：#B22234
#国旗蓝：#3C3B6E

import turtle
import math


def edge(x, y):
    turtle.penup()
    turtle.goto(x - 190, y + 100)  # 起始位置
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('#B22234')
    turtle.pen(pencolor='#B22234')
    for i in range(2):
        turtle.fd(380)
        turtle.right(90)
        turtle.fd(200)
        turtle.right(90)
    turtle.end_fill()  # 绘制国旗红面矩形
    turtle.penup()

    for i in range(6):
        turtle.goto(-190, 100 - 200 / 13 * (2 * i + 1))
        turtle.forward(0)

        turtle.begin_fill()  # 绘制白条纹
        turtle.fillcolor('#FFFFFF')  # 绘制白条纹
        turtle.pen(pencolor='#FFFFFF')
        for j in range(2):
            turtle.fd(381)
            turtle.right(90)
            turtle.fd(200 / 13)
            turtle.right(90)
        turtle.end_fill()  # 绘制白条纹

    turtle.penup()

    turtle.goto(-190, 100)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('#3C3B6E')
    turtle.pen(pencolor='#3C3B6E')
    for i in range(2):
        turtle.fd(380 / 5 * 2)
        turtle.right(90)
        turtle.fd(199 / 13 * 7)  # 这里参数本来是200，我看绘图多出来一块，于是就弄得199，因为这个1/13的比例他算的可能不是很精确
        turtle.right(90)
    turtle.end_fill()  # 绘制国旗蓝色
    turtle.penup()


def star():
    for i in range(9):
        if i % 2 == 0:
            for j in range(6):
                turtle.penup()
                turtle.goto(-190 + 380 / 5 * 2 / 12 * (2 * j + 1), 100 - (200 / 13 * 7) / 10 * (i + 1))
                turtle.setheading(90)
                turtle.fd(12.32 / 2 * math.cos(18 * math.pi / 180))
                turtle.left(162)
                turtle.pendown()
                turtle.pen(pencolor='#FFFFFF')

                turtle.begin_fill()
                turtle.fillcolor('#FFFFFF')
                for n in range(5):
                    turtle.fd(12.32 * math.cos(18 * math.pi / 180))
                    turtle.left(144)

                turtle.end_fill()  # 填充白色星星
        else:
            for j in range(5):
                turtle.penup()
                turtle.goto(-190 + 380 / 5 * 2 / 12 * (2 * j + 2), 100 - (200 / 13 * 7) / 10 * (i + 1))
                turtle.setheading(90)
                turtle.fd(12.32 / 2 * math.cos(18 * math.pi / 180))
                turtle.left(162)
                turtle.pendown()
                turtle.pen(pencolor='#FFFFFF')

                turtle.begin_fill()
                turtle.fillcolor('#FFFFFF')
                for n in range(5):
                    turtle.fd(12.32 * math.cos(18 * math.pi / 180))
                    turtle.left(144)

                turtle.end_fill()  # 填充白色星星


if __name__ == '__main__':
    turtle.setup(width=468, height=312)  # 左右两侧留出90像素距离 上下两侧留出60像素距离
    turtle.hideturtle()
    turtle.pen(speed=10)
    edge(0, 0)
    star()

turtle.done()