import math
from random import choice
from random import randint as rnd

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
DARK_GREEN = 0x009900
LIGHT_BLUE = 0x66ffff
BACKGROUND = 0xe0e0e0
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
delta = 10
gun_width = 10

g = 1           # гравитация
k = 0.5         # коэф угасания скорости при отражении от стенок
pi = math.pi



def rotated_rect(x, y, a, b, angle, screen, color):
    ''' Рисует прямоугольник, повернутый на angle (в радианах)'''
    cos = math.cos(angle)
    sin = math.sin(angle)
    pygame.draw.polygon(screen, color,
                        [(x-a/2*cos, y-a/2*sin), (x + a/2*cos, y + a/2*sin),
                         (x + a/2*cos + b*sin, y + a/2*sin - b*cos), (x + b*sin - a/2*cos, y - b*cos - a/2*sin)])


def star(x, y, r, R, color):
    ''' Рисует пятиконечную звезду с центром в (x,y) и радиусами вершин r и R. '''
    x0, x1, x2, x3, x4 = [(x+R*math.cos(pi/2 +2*pi/5*k),
                           y+R*math.sin(pi/2 +2*pi/5*k)) for k in range(5)]
    y0, y1, y2, y3, y4 = [(x+r*math.cos(pi/2 +2*pi/5*k + pi/5),
                           y+r*math.sin(pi/2 +2*pi/5*k + pi/5)) for k in range(5)]
    pygame.draw.polygon(screen, color, [x0, y0, x1, y1, x2, y2, x3, y3, x4, y4])


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450, creator = None):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 12
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.creator = creator

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy += -g

        ''' Отражение от нижней и правой стенок, как в зашифрованном коде'''
        if (self.y + self.r > HEIGHT - 30):
            self.y = HEIGHT - self.r - 30
            self.vy = -k*self.vy
            self.vx = k*self.vx
            if (self.vx**2 + self.vy**2 < 3):
                self.vx = 0
                self.vy = 0
        if (self.x > WIDTH):
            self.x = WIDTH
            self.vx = -k*self.vx
            self.vy = k*self.vy
        
            

    def draw(self):
        ''' Рисует шарик и черную границу. '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width = 2
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в объекте obj.

        Args:
            obj: Объект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.x = 100
        self.y = 450
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.health = 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, x = self.x, y = self.y)
        new_ball.r += 1
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)/2
        new_ball.vy = - self.f2_power * math.sin(self.an)/2
        new_ball.creator = 'gun'
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan2(event.pos[1]-self.y, event.pos[0]-20 - self.x)
            except:
                ZeroDivisionError
                print(ZeroDivisionError)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        ''' Рисует очень красивый и реалистичный танк. '''
        rotated_rect(self.x, self.y, gun_width, 20 + 0.4*self.f2_power, self.an + math.pi/2, self.screen, self.color)
        pygame.draw.rect(self.screen, DARK_GREEN, (self.x-40, self.y, 80, 30))
        pygame.draw.circle(self.screen, DARK_GREEN, (self.x, self.y), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x-20, self.y+35), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x+20, self.y+35), 10)
        star(self.x, self.y+13, 15, 5, RED)
        

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 55:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self):
        ''' Двигает танк по горизонатли. '''
        global direction
        self.x += 2*direction
        if self.x < 50:
            self.x = 50
        if self.x > WIDTH - 50:
            self.x = WIDTH - 50

    def hittest(self, obj):
        ''' Возвращает True, если шарик (obj) пересекает корпус танка (прямоугольник). '''
        ans = False
        x_rel = obj.x - self.x
        y_rel = obj.y - self.y
        r = obj.r

        if (((x_rel+40)**2 + y_rel**2 <= r**2)
            or ((x_rel-40)**2 + y_rel**2 <= r**2)
            or ((x_rel+40)**2 + (y_rel-30)**2 <= r**2)
            or ((x_rel-40)**2 + (y_rel-30)**2 <= r**2)):
            ans = True

        if ((-40 <= x_rel) and (x_rel <= 40) and (-r <= y_rel) and (y_rel <= 40+r)):
            ans = True

        if ((-40-r <= x_rel) and (x_rel <= 40+r) and (0 <= y_rel) and (y_rel <= 40)):
            ans = True

        if (obj.live >= 25 and obj.creator == 'gun'):
            ans = False
        
        return ans

        

class Target(Ball):
    def __init__(self, screen: pygame.Surface):
        """ Инициализация новой цели. """
        self.screen = screen
        self.live = 1
        self.points = 0
        self.time = 0

        self.vy = rnd(-5, 5)

        global targets
        self.r = rnd(20, 50)
        self.color = RED
        
        finished = False
        while not finished:
            self.x = rnd(600, 780)
            self.y = rnd(300, 550)
            ok = True
            for t in targets:
                if self.hittest(t): ok = False
            if ok: finished = True
                
                

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Не учитывает гравитацию
        """
        self.y -= self.vy

        if (self.y < self.r):
            self. y = self.r
            self.vy = -self.vy

        if (self.y > HEIGHT - self.r):
            self.y = HEIGHT - self.r
            self.vy = -self.vy

class UFO:
    def __init__(self, screen):
        self.health = 3
        self.y = rnd(0, 100)
        self.x = rnd(50, WIDTH-250)
        self.vx = rnd(-10, 10)
        self.screen = screen
        self.death_time = 30
        self.time = 0

    def draw(self):
        x = self.x
        y = self.y
        pygame.draw.circle(self.screen, LIGHT_BLUE, (x+100, y+100), 50)
        pygame.draw.rect(self.screen, BACKGROUND, (x+50, y+100, 100, 50))
        pygame.draw.polygon(self.screen, GREY, [(x+50, y+100), (x+0, y+130), (x+200, y+130),
                                           (x+150, y+100)])
        if self.health == 3:
            pygame.draw.circle(self.screen, GREEN, (x+50, y+115), 10)
        else:
            pygame.draw.circle(self.screen, RED, (x+50, y+115), 10)
        if self.health >= 2:
            pygame.draw.circle(self.screen, GREEN, (x+100, y+115), 10)
        else:
            pygame.draw.circle(self.screen, RED, (x+100, y+115), 10)
        if self.health >= 1:
            pygame.draw.circle(self.screen, GREEN, (x+150, y+115), 10)
        else:
            
            pygame.draw.circle(self.screen, RED, (x+150, y+115), 10)

    def move(self):
        self.x += self.vx

        if self.x < 50:
            self.x = 50
            self.vx = -self.vx
        if self.x > WIDTH - 250:
            self.x = WIDTH - 250
            self.vx = -self.vx
            
    def hittest(self, obj):
        ans = False
        x_rel = obj.x - self.x
        y_rel = obj.y - self.y
        r = obj.r

        # check with the light blue demicircle
        if (((x_rel - 100)**2 + (y_rel - 100)**2 <= (r + 50)**2) and (y_rel <= + 100)):
            ans = True

        # check if close to angles of the grey polygon
        if ((x_rel-50)**2 + (y_rel-100)**2 <= r**2):
            ans = True
        if ((x_rel-0)**2 + (y_rel-130)**2 <= r**2):
            ans = True
        if ((x_rel-200)**2 + (y_rel-130)**2 <= r**2):
            ans = True
        if ((x_rel-150)**2 + (y_rel-100)**2 <= r**2):
            ans = True

        # last check for being near the polygon
        if ((x_rel <= 150) and (x_rel >= 50) and (y_rel <= 100) and (y_rel >= 100 - r)):
            ans = True
        if ((x_rel <= 200) and (x_rel >= 0) and (y_rel >= 130) and (y_rel <= 130 + r)):
            ans = True
            
        sin = 30 / (50**2 + 30**2)**(1/2)
        cos = 50 / (50**2 + 30**2)**(1/2)
        l = (50**2 + 30**2)**(1/2)
        
        x_weird = x_rel * cos - (y_rel-130) * sin
        y_weird = -x_rel * sin - (y_rel-130) * cos
        if ((x_weird >= 0) and (x_weird <= l) and (y_weird >= 0) and (y_weird <= r)):
            ans = True

        x_weird = -(x_rel - 200) * cos - (y_rel - 130) * sin
        y_weird = (x_rel - 200) * sin - (y_rel - 130) * cos
        if ((x_weird >= 0) and (x_weird <= l) and (y_weird >= 0) and (y_weird <= r)):
            ans = True

        if obj.creator == 'ufo':
            ans = False

        return ans
        

def background():
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, GREEN, (0, 485, WIDTH, HEIGHT - 485))
    


    

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myfont = pygame.font.SysFont(None, 60)
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
#target = Target(screen)


targets = []
for i in range(0):
    temp = Target(screen)
    targets.append(temp)

enemies = []
for i in range(1):
    temp = UFO(screen)
    enemies.append(temp)

time = 0
direction = 0
result = 0
finished = False

while not finished:
    background()
    gun.draw()
    for e in enemies:
        e.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()

    # Вывода здоровья на экран
    text = "Your health: " + str(gun.health)
    textsurface = myfont.render(text, False, BLACK)
    screen.blit(textsurface, (0, 0))
    

    pygame.display.update()

    
    gun.move()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if ((event.unicode == 'd') or (event.scancode == 79) or (event.scancode == 7)):
                direction = 1
            if ((event.unicode == 'a') or (event.scancode == 80) or (event.scancode == 4)):
                direction = -1
            if ((event.unicode == 'w') or (event.unicode == 's')
                or (event.scancode == 26) or (event.scancode == 22)
                or (event.scancode == 82) or (event.scancode == 81)):
                direction = 0
            

    for e in enemies:
        e.move()
    
    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()
                targets.remove(t)
                targets.append(Target(screen))
        for e in enemies:
            if e.hittest(b):
                e.health -= 1
                b.live -= 30

        if gun.hittest(b):
            gun.health -= 1
            b.live -= 30
    gun.power_up()
    

    

    

    time += 1

    

    # Убираем старые шарики
    for b in balls:
        b.live -= 0.2
        if b.live <= 0:
            balls.remove(b)

    # Убираем сломанные ufo
    for e in enemies:
        if e.health <= 0:
            e.death_time -= 1
        if e.death_time <= 0:
            enemies.remove(e)
            enemies.append(UFO(screen))
            result += 1

    # Бросаем рандомно снаряды из ufo
    average_time = 1000
    for e in enemies:
        e.time += 1
        if rnd(0, average_time) <= e.time:
            temp = Ball(screen, x = e.x + 100, y = e.y + 130, creator = 'ufo')
            temp.vx = rnd(-10, 10)
            balls.append(temp)
            e.time = 0

    if gun.health <= 0:
        finished = True

time2 = 0

while time2 <= 10*FPS:
    clock.tick(FPS)
    background()

    text1 = "You have destroyed " + str(result) + " enemies"
    surface1 = myfont.render(text1, False, BLACK)
    screen.blit(surface1, (0, 0))
    
    if result == 0:
        text2 = "Comrade Stalin will not be pleased"
        surface2 = myfont.render(text2, False, BLACK)
        screen.blit(surface2, (0, 30))
    
    if result >= 5:
        text2 = "Well done, comrade"
        surface2 = myfont.render(text2, False, BLACK)
        screen.blit(surface2, (0, 50))
    
    pygame.display.update()

    time2 += 1

    
    
        

    





pygame.quit()
