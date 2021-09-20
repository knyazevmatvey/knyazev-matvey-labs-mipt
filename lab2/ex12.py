import turtle

def halfcircle(r):
    for i in range(50):
        turtle.forward(4*r)
        turtle.left(180/50)

turtle.shape('turtle')
turtle.speed(0)
turtle.right(90)
for i in range(10):
    halfcircle(1)
    halfcircle(0.2)
