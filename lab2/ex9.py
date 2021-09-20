import turtle
import math

def polyangle(n, s):
    l = 2*math.sin(2*math.pi/(2*n))*s
    turtle.penup()
    turtle.forward(s)
    turtle.left(180)
    turtle.right(90*(n-2)/n)
    turtle.right(360/n)
    turtle.pendown()
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(l)
    turtle.penup()
    turtle.left(360/n)
    turtle.left(90*(n-2)/n)
    turtle.forward(s)
    turtle.left(180)

turtle.shape('turtle')
turtle.speed(0)
for n in range(3, 13, 1):
    polyangle(n, 25*(n-1))
