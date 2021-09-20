import turtle
import math

turtle.shape('turtle')
turtle.speed(0)

def star_n(n):
    r = 200
    phi = 2*math.pi/n
    turtle.penup()
    turtle.goto(r*math.sin(phi), r*math.cos(phi))
    turtle.left(180)
    s = 2*r*math.sin(phi)
    turtle.pendown()
    for i in range(n):
        turtle.forward(s)
        turtle.left(180)
        turtle.right(360/2/n)

n = int(input('n = '))
star_n(n)
