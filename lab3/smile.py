import pygame
from pygame.draw import *
import math

pygame.init()

#creating screen and choosing its size
a = 800
b = 800
screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 204, 102)
blue = (153, 255, 255)
gray = (160, 160, 160)
head = (224, 224, 224)
yellow = (255, 255, 0)
red = (255, 0, 0)
brown = (102, 51, 0)
pink = (255, 0, 255)


#gray backgorund
rect(screen, gray, (0, 0, a, b))

#big yellow circle
ellipse(screen, yellow, (a/4, b/4, a/2, b/2))

#mouth
width = 0.22 * a
height = 0.04 * b
x = (0.5 - width/a/2)
y = 0.62
rect(screen, black, (a*x, b*y, width, height))

#eyes
y = 0.42
dx = 0.12 #distance from x=a/2 to eye center
R = 0.042*a
r = 0.02*a

ellipse(screen, red, (a/2 + a*dx - R, y*a - R, 2*R, 2*R))
ellipse(screen, red, (a/2 - a*dx - R, y*a - R, 2*R, 2*R))
ellipse(screen, black, (a/2 + a*dx - r, y*a - r, 2*r, 2*r))
ellipse(screen, black, (a/2 - a*dx - r, y*a - r, 2*r, 2*r))

#right (from our point of view) eyebrow
ang = 0.24
width = 0.21 * a
height = 0.026 * a
x = 0.57
y = 0.40

cos = math.cos(ang)
sin = math.sin(ang)

polygon(screen, black, [(x*a, y*a), (x*a + width*cos, y*a - width*sin),
                        (x*a + width*cos - height*sin, y*a - width*sin - height*cos),
                        (x*a - height*sin, y*a - height*cos)])

#right (from our point of view) eyebrow
ang = math.pi - 0.49
width = 0.21 * a
height = 0.026 * a
x = 0.44
y = 0.39

cos = math.cos(ang)
sin = math.sin(ang)

polygon(screen, black, [(x*a, y*a), (x*a + width*cos, y*a - width*sin),
                        (x*a + width*cos - height*sin, y*a - width*sin - height*cos),
                        (x*a - height*sin, y*a - height*cos)])













pygame.display.update()

while True:
    for event in pygame.event.get():
        clock.tick(30)
        if event.type == pygame.QUIT:
            pygame.quit()
