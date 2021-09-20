import turtle

turtle.shape('turtle')
turtle.speed(10)
for i in range(11):
    step = i*10
    turtle.penup()
    turtle.forward(step)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(2*step)
    turtle.left(90)
    turtle.forward(2*step)
    turtle.left(90)
    turtle.forward(2*step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
