from turtle import Turtle
t=Turtle()
t.speed(1)
t.screen.bgcolor('black')
t.pencolor('yellow')
t.begin_fill()
for i in range(5):
    t.forward(110)
    t.left(144)
    t.fillcolor('gold')
t.end_fill()
