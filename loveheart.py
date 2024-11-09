from turtle import *

# 设置画笔速度和背景颜色
speed(5)
bgcolor("white")

# 绘制大红色爱心
color("red")
pensize(3)
penup()
goto(-80, 0)  # 定位到大爱心的起始位置
pendown()

begin_fill()
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

# 绘制小粉色爱心
color("pink")
penup()
goto(80, -20)  # 定位到小爱心的起始位置
setheading(50)  # 重置角度
pendown()

begin_fill()
forward(80)
circle(30, 200)
right(140)
circle(30, 200)
forward(80)
end_fill()

# 隐藏画笔并保持窗口打开
hideturtle()
done()
