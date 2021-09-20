import turtle

def circle(r):
    for i in range(100):
        turtle.forward(5*r)
        turtle.left(360/100)

turtle.shape('turtle')
turtle.speed(0)
for i in range(10):
    circle(1+0.1*i)
    turtle.left(180)
    circle(1+0.1*i)
    turtle.left(180)
