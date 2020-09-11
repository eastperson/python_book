radius = 50

def move(turtle,x,y) :
    p = turtle
    p.up()
    p.goto(x,y)
    p.down()


import turtle
t = turtle.Turtle()
t.shape("turtle")
move(t,0,0)
t.circle(radius)
move(t,100,0)
radius += 20
t.circle(radius)
move(t,200,0)
radius += 20
t.circle(radius)