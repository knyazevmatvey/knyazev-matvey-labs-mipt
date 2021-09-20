from random import randint
import turtle
import math

# parameters
number_of_turtles = 15
time = 100000
s = 300
v = 30
r = 22

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

# drawing borders
first = pool[0]
first.penup()
first.goto(-s, -s)
first.pendown()
first.goto(s, -s)
first.goto(s, s)
first.goto(-s, s)
first.goto(-s, -s)

# initial placing
x = [randint(-s, s) for i in range(number_of_turtles)]
y = [randint(-s, s) for i in range(number_of_turtles)]
v_x = [randint(-v, v) for i in range(number_of_turtles)]
v_y = [randint(-v, v) for i in range(number_of_turtles)]
    
for i in range(number_of_turtles):
    unit = pool[i]
    unit.penup()
    unit.speed(100000)
    unit.goto(x[i], y[i])


# moving
dt = 0.1
for i in range(time):
    
    # moving + reflections
    for j in range(number_of_turtles):
        unit = pool[j]
        x[j] += v_x[j] * dt
        y[j] += v_y[j] * dt
        
        # reflection
        if x[j] > s:
            x[j] = s
            v_x[j] = -v_x[j]
        if x[j] < -s:
            x[j] = -s
            v_x[j] = -v_x[j]
        if y[j] > s:
            y[j] = s
            v_y[j] = -v_y[j]
        if y[j] < -s:
            y[j] = -s
            v_y[j] = -v_y[j]

        unit.goto(x[j], y[j])

    # collisions with energy and momentum conversation
    for i in range(number_of_turtles):
        for j in range(i+1, number_of_turtles):
            if (x[i]-x[j])**2 + (y[i]-y[j])**2 < r**2:
                vx = (v_x[i] + v_x[j]) / 2
                vy = (v_y[i] + v_y[j]) / 2

                ux = (v_x[i] - v_x[j]) / 2
                uy = (v_y[i] - v_y[j]) / 2
                u = (ux**2 + uy**2)**(0.5)

                ang = randint(0, 360) / 360 * 2*math.pi
                print(v_x[i]**2 + v_x[j]**2 + v_y[i]**2 + v_y[j]**2)
                print(v_x[i] + v_x[j], v_y[i] + v_y[j])
                ux = u * math.cos(ang)
                uy = u * math.sin(ang)


                v_x[i] = vx + ux
                v_x[j] = vx - ux
                v_y[i] = vy + uy
                v_y[j] = vy - uy
                
                
                
            
            
    
