import turtle

turtle.shape('turtle')
s = 10
for i in range(10):
    step = s*(1+2*i)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(s + step)
    turtle.left(90)
    turtle.forward(s + step)
    turtle.left(90)
