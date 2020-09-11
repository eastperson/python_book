side = 100
angle = 90
import turtle
t = turtle.Turtle()
t.shape("turtle")

def rightDown(turtle,side,angle):
    p = turtle
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)

def rightUp(turtle,side,angle) :
    p = turtle
    p.forward(side)
    p.left(angle)
    p.forward(side)
    p.left(angle)
    p.forward(side)
    p.left(angle)
    p.forward(side)
    p.left(angle)

def leftUp(turtle,side,angle) :
    p = turtle
    p.left(180)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.right(90)

def leftDown(turtle,side,angle) :
    p = turtle
    p.right(90)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)
    p.forward(side)
    p.right(angle)


rightUp(t,side,angle)
rightDown(t,side,angle)
leftUp(t,side,angle)
leftDown(t,side,angle)