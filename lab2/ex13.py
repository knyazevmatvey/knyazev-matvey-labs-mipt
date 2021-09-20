import turtle
import math

def halfcircle(r):
    for i in range(50):
        turtle.forward(5*r)
        turtle.left(180/50)

def circle(r):
    for i in range(100):
        turtle.forward(5*r)
        turtle.left(360/100)

def circle_from_center(r):
    ss = r*5/(math.pi/50)
    turtle.penup()
    turtle.forward(ss)
    turtle.pendown()
    turtle.left(90)
    turtle.begin_fill()
    circle(r)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(ss)
    turtle.left(180)

turtle.shape('turtle')
turtle.speed(0)


# рисуем круг и возвращаемся
R = 5/(math.pi/50)
turtle.color('yellow')
circle_from_center(1)

# глаза
turtle.left(50)
turtle.color('blue')
turtle.forward(0.5*R)
circle_from_center(0.2)
turtle.left(180)
turtle.forward(0.5*R)
turtle.left(180)
turtle.left(80)
turtle.color('blue')
turtle.forward(0.5*R)
circle_from_center(0.2)
turtle.left(180)
turtle.forward(0.5*R)
turtle.left(50)

# нос
turtle.right(90)
turtle.forward(0.2*R)
turtle.left(180)
turtle.color('black')
turtle.width(10)
turtle.pendown()
turtle.forward(0.4*R)
turtle.penup()
turtle.left(180)
turtle.forward(0.2*R)
turtle.left(90)

# рот
turtle.left(180)
turtle.forward(0.7*R)
turtle.left(90)
turtle.pendown()
turtle.color('red')
halfcircle(0.7)


