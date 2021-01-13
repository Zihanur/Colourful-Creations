from turtle import *
screen = Screen()
screen.setup(400,400)
screen.bgcolor("orange")

penup()
goto(0,100)
color("red")
style = ('Arial',40,'bold')
write("HELLO", font=style, align='center')

right(90)
forward(60)
color("black")
write("ZIHAN", font=style, align='center')
hideturtle()