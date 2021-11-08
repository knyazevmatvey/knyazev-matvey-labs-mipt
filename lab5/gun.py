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
LIGHT_BLUE = 0x66ffff
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
delta = 10
gun_width = 10

g = 1           # гравитация
k = 0.5         # коэф угасания скорости при отражении от стенок



def rotated_rect(x, y, a, b, angle, screen, color):
    ''' Рисует прямоугольник, повернутый на angle (в радианах)'''
    cos = math.cos(angle)
    sin = math.sin(angle)
    pygame.draw.polygon(screen, color,
                        [(x, y), (x + a*cos, y + a*sin),
                         (x + a*cos + b*sin, y + a*sin - b*cos), (x + b*sin, y - b*cos)])

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

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
        if (self.y + self.r > HEIGHT):
            self.y = HEIGHT - self.r
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
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            except:
                ZeroDivisionError
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        rotated_rect(20, 450, gun_width, 20 + 0.8*self.f2_power, self.an + math.pi/2, self.screen, self.color)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


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
    def __init__(self):
        self.health = 3
        self.y = rnd(0, 100)
        self.x = rnd(50, WIDTH-250)
        self.vx = rnd(-10, 10)

    def draw(self):
        x = self.x
        y = self.y
        pygame.draw.circle(screen, LIGHT_BLUE, (x+100, y+100), 50)
        pygame.draw.rect(screen, WHITE, (x+50, y+100, 100, 50))
        pygame.draw.polygon(screen, GREY, [(x+50, y+100), (x+0, y+130), (x+200, y+130),
                                           (x+150, y+100)])
        if self.health == 3:
            pygame.draw.circle(screen, GREEN, (100, 115), 10)
        else:
            pygame.draw.circle(screen, RED, (100, 115), 10)
        if self.health >= 2:
            pygame.draw.circle(screen, GREEN, (50, 115), 10)
        if self.health >= 1:
            pygame.draw.circle(screen, GREEN, (150, 115), 10)

    def move(self):
        self.x += self.vx

        if self.x < 0:
            self.x = 0
            self.vx -= self.vx
        if self.x > WIDTH - 200:
            self.x = WIDTH - 200
            self.vx -= self.vx
        



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
#target = Target(screen)
finished = False

targets = []
for i in range(2):
    temp = Target(screen)
    targets.append(temp)

enemies = []
for i in range(1):
    temp = UFO()
    enemies.append(temp)

time = 0

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

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

    for t in targets:
        t.move()
        #t.time += 1
        #if (t.time % FPS == 0):
        #    t.vy = -t.vy
    
    for b in balls:
        for t in targets:
            b.move()
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()
                targets.remove(t)
                targets.append(Target(screen))
    gun.power_up()

    for e in enemies:
        e.draw()
        e.move()

    # Убираем старые шарики
    for b in balls:
        b.live -= 0.6
        if b.live <= 0:
            balls.remove(b)

    

    time += 1

    



pygame.quit()
