from turtle import Turtle
t=Turtle()
t.speed(1)
t.screen.bgcolor('yellow')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
    t.fillcolor('red')
t.end_fill()

t.screen.exitonclick()
