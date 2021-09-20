import turtle

def circle():
    for i in range(100):
        turtle.forward(5)
        turtle.left(360/100)

turtle.shape('turtle')
turtle.speed(0)
n = 6
for i in range(n):
    circle()
    turtle.left(360/n)
