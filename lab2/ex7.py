import turtle

turtle.shape('turtle')
turtle.speed(0)
step = 0.01
for i in range(1000):
    turtle.forward(i*step)
    turtle.left(2)
