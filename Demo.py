#因为3:2非美国国旗标准比例
#以下计算数据均不为官方数据
#也不为计算数据。。。（纯目测出来的dogo

#导入turtle
from turtle import *

#基础数据的准备
a=1200
b=800
c=b/13
d=a*5/11
e=d/11
f=7*c/9
n=0

#准备工作1
setup(a,b)
pensize(c)
speed(0)
up()
goto(-a/2,b/2-c/2)
down()

#不在画布内就装作看不到的偷懒式简单红色条纹QwQ
color("red")
fd(a)
while n<=20:
    n+=4
    g=b-n*c
    up()
    goto(-a/2,g/2-c/2)
    down()
    fd(a)

#准备工作2
up()
goto(-a/2,b/2)
fillcolor("blue")
begin_fill()
for i in range(2):
    fd(d)
    rt(90)
    fd(7*c)
    rt(90)
end_fill()
down()
pensize(1)
color("white")

#白色星星1
for j in range(5):
    up()
    goto(-a/1.8,b/2-c/2-1.4*j*c)
    down()
    for k in range(6):
        up()
        fd(e*1.8)
        down()
        fillcolor("white")
        begin_fill()
        for l in range(5):
            fd(e/3.8)
            lt(72)
            fd(e/3.8)
            rt(144)
        end_fill()

#白色星星2
for j in range(4):
    up()
    goto(-a/1.8+0.9*e,b/2-(1.4*(j+1)-0.2)*c)
    down()
    for k in range(5):
        up()
        fd(e*1.8)
        down()
        fillcolor("white")
        begin_fill()
        for l in range(5):
            fd(e/3.8)
            lt(72)
            fd(e/3.8)
            rt(144)
        end_fill()
#两种星星的画法好像用循环合并，但懒得思考了
#“‘ctrl+c’和‘ctrl+v’是计算机史上最伟大的发明--Fu_Dark”

hideturtle()