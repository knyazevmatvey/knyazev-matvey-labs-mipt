import turtle

turtle.shape('turtle')
turtle.speed(0)

#input
inp = open('numbers.txt', 'r')
numbers = [0 for j in range(10)]
for i in range(10):
    s = inp.readline()
    s = s.rstrip()
    numbers[i] = s


def draw(n, pos):
    num = numbers[n]
    coord = [20*int(x) for x in num.split()]
    turtle.penup()
    for i in range(len(coord) // 2):
        turtle.goto(coord[2*i] + pos, coord[2*i+1])
        turtle.pendown()

index = [1, 4, 1, 7, 0, 0]    
for i in range(len(index)):
    draw(index[i], i*30)
        
