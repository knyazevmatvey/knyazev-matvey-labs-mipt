import turtle

turtle.shape('turtle')
turtle.speed(0)
n = 12
for i in range(n):
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)
    turtle.left(360/n)
