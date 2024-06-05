from turtle import Turtle
t=Turtle()
t.speed(1)
color=['red','green','black','yellow','blue','magenta','orange']
t.pencolor()
for x in range(900):
    t.pencolor(color[x%6])
    t.forward(x)
    t.left(59)

t.screen.exitonClick()
