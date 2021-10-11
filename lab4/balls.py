import pygame
from pygame.draw import *
from random import randint

pygame.init()

h_res = 0
height = 800
width = 800
FPS = 120
dt = 1/FPS
screen = pygame.display.set_mode((width, height + h_res))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Balls:
    def __init__(self):
        self.r = randint(10, 50)
        self.v_x = randint(-100, 100)
        self.v_y = randint(-100, 100)
        #Color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = COLORS[randint(0, 5)] #Color #
        
        self.x = randint(30+r, width-30-r)
        self.y = randint(30+r, height-30-r)

        

    def move(self, times = 1):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def xyr(self):
        return self.x, self.y, self.r

    def vx_vy(self):
        return self.v_x, self.v_y

    def change_velocity(self, v1, v2):
        self.v_x = v1
        self.v_y = v2

    def change_position(self, x, y):
        self.x = x
        self.y = y

        

    def reflect_from_walls(self):
        if self.x > width - self.r:
            self.x = width - self.r
            self.v_x = - self.v_x
        if self.x < self.r:
            self.x = self.r
            self.v_x = - self.v_x
        if self.y > height - self.r:
            self.y = height - self.r
            self.v_y = - self.v_y
        if self.y < self.r:
            self.v_y = - self.v_y

    def show(self):
        circle(screen, self.color, (self.x, self.y), self.r)




def reflect_from_others():
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            ball1 = balls[i]
            ball2 = balls[j]
            x1, y1, r1 = ball1.xyr()
            x2, y2, r2 = ball2.xyr()
            v1_x, v1_y = ball1.vx_vy()
            v2_x, v2_y = ball2.vx_vy()
            m1 = r1 ** 2
            m2 = r2 ** 2

            if ((x1-x2)**2 + (y1-y2)**2 <= (r1 + r2)**2):
                l = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
                cos = -(x1 - x2) / l
                sin = -(y1 - y2) / l
                
                v1t = v1_x * cos + v1_y * sin
                v2t = v2_x * cos + v2_y * sin
                v1n = v1_x * sin - v1_y * cos
                v2n = v2_x * sin - v2_y * cos

                
                u1t = (2*m2*v2t - m2*v1t + m1*v1t) / (m1 + m2)
                u2t = (2*m1*v1t - m1*v2t + m2*v2t) / (m1 + m2)

                v1x = u1t * cos + v1n * sin
                v1y = u1t * sin - v1n * cos
                v2x = u2t * cos + v2n * sin
                v2y = u2t * sin - v2n * cos

                

                ball1.change_velocity(v1x, v1y)
                ball2.change_velocity(v2x, v2y)

                while ((x1-x2)**2 + (y1-y2)**2 <= (r1 + r2)**2):
                    ball1.move(0.02)
                    ball2.move(0.02)
                    x1, y1, r1 = ball1.xyr()
                    x2, y2, r2 = ball2.xyr()
                    

                
                
                





pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = []

t = 0
n = 0
for i in range(30):
    ball = Balls()
    balls.append(ball)
while not finished:
    screen.fill(BLACK)
    clock.tick(FPS)
    t += 1
    
     
    if (t % FPS == 0):
        ball = Balls()
        balls.append(ball)

    

    
    
    for ball in balls:
        ball.move()
        ball.reflect_from_walls()
        reflect_from_others()
        ball.show()

    hit = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = map(int, event.pos)
            for ball in balls:
                x, y, r = ball.xyr()
                if (x-x0)**2 + (y-y0)**2 <= r**2:
                    balls.remove(ball)
                    n += 1
                    hit = True

    if hit:
        print(n)
                    
       
    pygame.display.update()

pygame.quit()
