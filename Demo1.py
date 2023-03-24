#因为3:2比例导致的图形具体位置不规范
from turtle import *
a=1200
b=800
speed(0)
setup(a,b)
c=b/13
y=-b/2
n=0
t="red"
for n in range(13):
    up()
    goto(-a/2,y+n*c)
    pd()
    if n%2==0:
        C="red"
    else:
        C="white"
    color(C,C)
    begin_fill()
    for i in range(2):
        fd(a)
        lt(90)
        fd(c)
        lt(90)
    end_fill()
up()
goto(-a/2,y+7*c)
pd()
color("blue","blue")
begin_fill()
goto(0,c/2)
goto(0,-y)
goto(-a/2,-y)
goto(-a/2,y+6*c)
end_fill()
l=c/2
m=-l-y
n=a/2
u=n
n=n/35
m=m/10
for i in range(9):
    if i%2==0:
        i+=1
        up()
        goto(-u+n,-y-i*m)
        pd()
        for k in range(6):
            color("blue","white")
            begin_fill()
            for e in range(5):
                fd(n)
                lt(72)
                fd(n)
                rt(144)
            end_fill()
            up()
            fd(n*6)
            pd()
    else:
        i+=1
        up()
        goto(-u+4*n,-y-i*m)
        pd()
        for k in range(5):
            color("blue","white")
            begin_fill()
            for e in range(5):
                fd(n)
                lt(72)
                fd(n)
                rt(144)
            end_fill()
            up()
            fd(n*6)
            pd()
done()