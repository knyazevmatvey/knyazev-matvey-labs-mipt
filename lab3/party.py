import pygame
from pygame.draw import *
import math
pi = math.pi

pygame.init()

# creating screen and choosing its size
A = 1000
B = 800
screen = pygame.display.set_mode((A, B))

clock = pygame.time.Clock()


# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 204, 102)
blue = (153, 255, 255)
gray = (160, 160, 160)
head = (224, 224, 224)
yellow = (255, 214, 0)
red = (255, 0, 0)
brown = (102, 51, 0)
pink = (255, 0, 255)



#grass and sky
border = 0.58
rect(screen, green, (0, border*B, A, B - border*B))
rect(screen, blue, (0, 0, A, border*B))



# a, b - boy dimensions
# x and y move boy in x and y dircetions
def boy(x, y, a = 1000, b = 800):
    # body
    x1 = 0.30
    w = 0.15
    y1 = 0.38
    h = 0.37
    ellipse(screen, gray, (x1*a + x, y1*b + y, w*a, h*b))

    # head
    x1 += 0.02
    w -= 0.04
    y1 = 0.256
    h = 0.138
    ellipse(screen, head, (x1*a + x, y1*b + y, w*a, h*b))

    # legs
    x1 = 0.35
    y1 = 0.738
    x2 = 0.28
    y2 = 0.9325
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = x1 - 0.04
    y2 = y1 + 0.006
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = 0.400
    y1 = 0.738
    x2 = 0.42
    y2 = 0.925
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = x1 + 0.035
    y2 = y1 + 0.006
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    # arms
    x1 = 0.32
    y1 = 0.438
    x2 = x1 - 0.13
    y2 = y1 + 0.20
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = 0.43
    y1 = 0.444
    x2 = x1 + 0.11
    y2 = y1 + 0.20
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

# l defines dimensions of ice cream
# phi (in degrees) defines angle
# x and y move ice cream in x and y dircetions
def ice_cream(x, y, l, phi):
    phi = phi * (pi/180)
    alpha = pi/6 - phi
    x1 = x
    y1 = y
    x2 = x1 - l*math.cos(phi)
    y2 = y1 - l*math.sin(phi)
    x3 = x1 - l*math.sin(alpha)
    y3 = y1 - l*math.cos(alpha)
    polygon(screen, yellow, [(x1, y1), (x2, y2), (x3, y3)])

    d = 0.125 * l
    r = 0.25 * l
    x4 = x2 - 0.8*d*math.cos(phi + pi/6) + 2.2*d*math.cos(pi/3 - phi)
    y4 = y2 - 0.8*d*math.sin(phi + pi/6) - 2.2*d*math.sin(pi/3 - phi)
    circle(screen, brown, (x4, y4), r)

    x5 = x2 - 0.8*d*math.cos(phi + pi/6) + 5.8*d*math.cos(pi/3 - phi)
    y5 = y2 - 0.8*d*math.sin(phi + pi/6) - 5.8*d*math.sin(pi/3 - phi)
    circle(screen, red, (x5, y5), r)

    x6 = x2 - 3*d*math.cos(phi + pi/6) + 4*d*math.cos(pi/3 - phi)
    y6 = y2 - 3*d*math.sin(phi + pi/6) - 4*d*math.sin(pi/3 - phi)
    circle(screen, white, (x6, y6), r)



# a, b - girl dimensions
# x and y move girl in x and y dircetions
def girl(x, y, a=1000, b=800):
    # body
    x1 = 0.70
    y1 = 0.375
    x2 = 0.60
    y2 = 0.75
    x3 = 0.80
    y3 = 0.75
    polygon(screen, pink, [(x1*a + x, y1*b + y), (x2*a + x, y2*b + y),
                           (x3*a + x, y3*b + y)])

    # head
    x1 += 0.050
    x2 = x1 - 0.10
    y1 = 0.256
    y2 = 0.394
    ellipse(screen, head, (x1*a + x, y1*b + y, x2*a-x1*a, y2*b-y1*b))

    # legs
    x1 = 0.67
    y1 = 0.75
    x2 = x1
    y2 = 0.92
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = 0.63
    y2 = y1
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = 0.73
    y1 = 0.75
    x2 = x1
    y2 = 0.92
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = 0.77
    y2 = 0.926
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    #arms
    x1 = 0.686
    y1 = 0.42
    x2 = 0.52
    y2 = 0.64
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = 0.71
    y1 = 0.42
    x2 = 0.78
    y2 = 0.50
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x1 = 0.85
    y1 = 0.45
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)


# same as girl(), but here i replaced every x with -x, so for girl to be on the screen x
# should be large
def girl_reflected(x, y, a=1000, b=800):
    # body
    x1 = -0.70
    y1 = 0.375
    x2 = -0.60
    y2 = 0.75
    x3 = -0.80
    y3 = 0.75
    polygon(screen, pink, [(x1*a + x, y1*b + y), (x2*a + x, y2*b + y),
                           (x3*a + x, y3*b + y)])

    # head
    x1 -= 0.050
    x2 = x1 + 0.10
    y1 = 0.256
    y2 = 0.394
    ellipse(screen, head, (x1*a + x, y1*b + y, x2*a-x1*a, y2*b-y1*b))

    # legs
    x1 = -0.67
    y1 = 0.75
    x2 = x1
    y2 = 0.92
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = -0.63
    y2 = y1
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = -0.73
    y1 = 0.75
    x2 = x1
    y2 = 0.92
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x2 = -0.77
    y2 = 0.926
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    #arms
    x1 = -0.686
    y1 = 0.42
    x2 = -0.52
    y2 = 0.64
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = -0.71
    y1 = 0.42
    x2 = -0.78
    y2 = 0.50
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)

    x1 = x2
    y1 = y2
    x1 = -0.85
    y1 = 0.45
    line(screen, black, (x1*a + x, y1*b + y), (x2*a + x, y2*b + y), 2)



# l defines dimensions of heart
# phi (in degrees) defines angle
# x and y move heart in x and y dircetions
def heart(x, y, l, phi):
    r = 0.24 * l
    x0 = x
    y0 = y
    phi = phi * (pi/180)
    k = 0.30
    cos = math.cos(phi)
    sin = math.sin(phi)
    polygon(screen, red, [(x0, y0), (x0 + l*cos, y0 - l*sin),
                          (x0 + l*math.cos(phi + k*pi), y0 - l*math.sin(phi + k*pi))])

    x1 = x0 + l*cos - 0.25 * (l*2*math.sin(pi*k/2)) * math.cos((1-k)*pi/2 - phi)
    y1 = y0 - l*sin - 0.25 * (l*2*math.sin(pi*k/2)) * math.sin((1-k)*pi/2 - phi)
    circle(screen, red, (x1, y1), r)

    x2 = x0 + l*cos - 0.75 * (l*2*math.sin(pi*k/2)) * math.cos((1-k)*pi/2 - phi)
    y2 = y0 - l*sin - 0.75 * (l*2*math.sin(pi*k/2)) * math.sin((1-k)*pi/2 - phi)
    circle(screen, red, (x2, y2), r)


# main part
# left boy
boy(0, 200, 600, 480)

# left girl
girl(0, 200, 600, 480)

# right girl
girl_reflected(1016, 199, 600, 480)

# right boy
boy(580, 200, 600, 480)

# ice cream for the right boy
ice_cream(900, 515, 80, 95)

# big ice cream
ice_cream(530, 200, 120, 55)
line(screen, black, (507, 420), (530, 200), 2)

#heart for left boy
heart(70, 350, 100, 70)
line(screen, black, (120, 510), (70, 350), 2)


pygame.display.update()

while True:
    for event in pygame.event.get():
        clock.tick(30)
        if event.type == pygame.QUIT:
            pygame.quit()

            
