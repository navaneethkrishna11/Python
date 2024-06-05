from turtle import Turtle
t=Turtle()
t.screen.bgcolor('green')
t.pencolor('yellow')
t.begin_fill()

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor('red')
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()


t.screen.exitonclick()


