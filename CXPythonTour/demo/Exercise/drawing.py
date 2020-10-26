#导入库
import turtle
import random

p = turtle


#定义画圆函数
def drawCircle(x, y, c='red'):

    p.pu()  # 抬起画笔
    p.goto(x, y)  # 绘制圆的起始位置
    p.pd()  # 放下画笔
    p.color(c)  # 绘制c色圆环
    p.circle(30, 360)  #绘制圆:半径，角度


#绘制雪花
def snow(snow_count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        p.pencolor(r, g, b)
        p.pu()
        p.goto(random.randint(-350, 350), random.randint(1, 270))
        p.pd()
        dens = random.randint(8, 12)
        snowsize = random.randint(10, 14)
        for _ in range(dens):
            p.forward(snowsize)
            p.backward(snowsize)
            p.right(360 / dens)


#绘制地面
def ground(ground_line_count):
    p.hideturtle()
    p.speed(500)
    for i in range(ground_line_count):
        p.pensize(random.randint(5, 10))
        x = random.randint(-400, 350)
        y = random.randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        p.pencolor(r, g, b)
        p.penup()
        p.goto(x, y)
        p.pendown()
        p.forward(random.randint(40, 100))


#主函数
def main():

    #绘制五环图
    # p.pensize(3)
    # drawCircle(0, 0, 'blue')
    # drawCircle(60, 0, 'black')
    # drawCircle(120, 0, 'red')
    # drawCircle(90, -30, 'green')
    # drawCircle(30, -30, 'yellow')
    # p.done()

    #雪花飘飘
    p.setup(800, 600, 0, 0)
    p.bgcolor('black')
    snow(30)
    ground(30)
    p.mainloop()


main()
