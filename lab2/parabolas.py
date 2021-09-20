import turtle

turtle.shape('turtle')
turtle.speed(0)

#horizontal line
turtle.goto(2000, 0)
turtle.goto(0, 0)

#initial values
x = 0
y = 0
v_x = 10
v_y = 50


#motion
dt = 0.1
a_y = -10
k = 0.8
for i in range(10000):
    
    #general case
    x += v_x * dt
    y += v_y * dt
    v_y += a_y * dt

    #reflection
    if y < 0:
        y = 0
        v_y = -v_y * k

    
    turtle.goto(x, y)
    
