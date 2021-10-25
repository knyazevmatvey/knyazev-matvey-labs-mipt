import pygame
from pygame.draw import *
from random import randint
import json

pygame.init()
myfont = pygame.font.SysFont(None, 60)

# некоторые из этих переменных еще не использованы, но могут быть потом
h_res = 0
height = 800
width = 800
FPS = 120
dt = 1/FPS
screen = pygame.display.set_mode((width, height + h_res))


# объявление цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Balls:
    '''
    Класс, содержащий шарики и связанные с ними функции
    '''
    def __init__(self):
        '''
        Инициализируются случайные радиус шарика, цвет и скорость.
        Координаты генерируются случайно, но шар не задевает границы и имеет
        отступ от них хотя бы в 30.
        '''
        self.r = randint(20, 50)
        self.v_x = randint(-100, 100)
        self.v_y = randint(-100, 100)
        self.color = COLORS[randint(0, 5)] 
        
        self.x = randint(80+self.r, width-80-self.r)
        self.y = randint(80+self.r, height-80-self.r)

        

    def move(self, times = 1):
        '''
        Передвигает шарик согласно его скорости, при этом dt=1/FPS выбрано так,
        что численное значение скорости совпадает с перемещением за 1 с
        '''
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def xyr(self):
        '''
        Функция, возвращающая координаты и радус
        '''
        return self.x, self.y, self.r

    def vx_vy(self):
        '''
        Функция, возвращающая компоненты скорости
        '''
        return self.v_x, self.v_y

    def change_velocity(self, v1, v2):
        '''
        Функция изменяет скорость на заданную
        '''
        self.v_x = v1
        self.v_y = v2

    def change_position(self, x, y):
        '''
        Функция изменяет координаты на заданные
        (Не используется в программе)
        '''
        self.x = x
        self.y = y

        

    def reflect_from_walls(self):
        '''
        Функция отражает все шарики от стен
        '''
        delta = 10
        if self.x > width - self.r:
            #self.x = width - self.r
            self.v_x = - self.v_x - delta
        if self.x < self.r:
            #self.x = self.r
            self.v_x = - self.v_x + delta
        if self.y > height - self.r:
            #self.y = height - self.r
            self.v_y = - self.v_y - delta
        if self.y < self.r:
            #self.y = self.r
            self.v_y = - self.v_y + delta

    def show(self):
        '''
        Функция рисует шарик
        '''
        circle(screen, self.color, (self.x, self.y), self.r)




def reflect_from_others():
    '''
    Функция проверяет все шарики на пересечение и пересекающиеся шарики отражает
    друг от друга
    При этом соударение происходит будто массы шаров пропорциональны их площадям,
    а сила во время удара направлено вдоль линии, соединяющей центры
    '''
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

                # отвечает за скачки
                while ((x1-x2)**2 + (y1-y2)**2 <= (r1 + r2)**2):
                    ball1.move(0.02)
                    ball2.move(0.02)
                    x1, y1, r1 = ball1.xyr()
                    x2, y2, r2 = ball2.xyr()
                    

                
                

class Square():
    '''
    Класс, содержащий квадраты и их функции
    Квадраты отражаются независимо от шаров и когда шар находится внутри квадрата, квадрат его
    съедает
    '''

    def __init__(self):
        self.a = 50
        #self.a = randint(40, 100)
        self.color = COLORS[randint(0, 5)]
        self.v_x = randint(-100, 100)
        self.v_y = randint(-100, 100)

        self.x = randint(30 + self.a, width - 30 - self.a)
        self.y = randint(30 + self.a, height - 30 - self.a)

        self.worth = 1

    def move(self):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def reflect_from_walls(self):
        if self.x > width - self.a:
            self.x = width - self.a
            self.v_x = randint(-100, -50)
        if self.x < self.a:
            self.x = self.a
            self.v_x = randint(50, 100)
        if self.y > height - self.a:
            self.y = height - self.a
            self.v_y = randint(-100, -50)
        if self.y < self.a:
            self.y = self.a
            self.v_y = randint(50, 100)

    def show(self):
        rect(screen, self.color, (self.x - self.a, self.y - self.a, 2*self.a, 2*self.a), 2)
                


def eating_time():
    for sq in squares:
        for ball in balls:
            if ((ball.x + ball.r < sq.x + sq.a)
                and (ball.x - ball.r > sq.x - sq.a)
                and (ball.y + ball.r < sq.y + sq.a)
                and (ball.y - ball.r > sq.y - sq.a)):
                balls.remove(ball)
                sq.worth += 1
                rect(screen, sq.color, (sq.x - sq.a, sq.y - sq.a, 2*sq.a, 2*sq.a), 0)
                sq.a += 2



pygame.display.update()
clock = pygame.time.Clock()
finished = False

# массив, который будет содержать активные (не выбывшие) шарики
balls = []
squares = []

t = 0
n = 0

# генерируем 30 шариков
for i in range(30):
    ball = Balls()
    balls.append(ball)

# генериреум квадрат
for i in range(1):
    sq = Square()
    squares.append(sq)




rate = 5
while not finished:
    screen.fill(BLACK)
    clock.tick(FPS)
    t += 1

    
    # каждую секунду добавляем шарик
    if ((rate*t) % FPS == 0):
        ball = Balls()
        balls.append(ball)
        intersection = False
        for ball2 in balls:
            if ball2 != ball:
                if ((ball.x - ball2.x)**2 + (ball.y - ball2.y)**2 < (ball.r + ball2.r)**2):
                    intersection = True
        if intersection:
            balls.remove(ball)
            

    
    # двигаем шарики и отражаем
    reflect_from_others()
    for ball in balls:
        ball.reflect_from_walls()
        ball.move()
        ball.show()

    for sq in squares:
        sq. reflect_from_walls()
        sq.move()
        sq.show()

    eating_time()

    
        
    # убираем из массива шарики, по которым попал игрок
    # повышаем счет на количество убитых шаров
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
    
        
    
    textsurface = myfont.render("You: " + str(n) + ", Square = "+ str(squares[0].worth), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))

    if 2*squares[0].a >= width:
        finished = True
        
    pygame.display.update()


# end sequence
t = 0
finished = False
while not finished:
    t += 1
    clock.tick(FPS)
    screen.fill(squares[0].color)
    text = "You: " + str(n) + ", Square: "+ str(squares[0].worth)
    end = "Game ends since"
    textsurface = myfont.render(text, False, (255, 255, 255))
    endsurface = myfont.render(end, False, (255, 255, 255))
    end2 = myfont.render("the Square has become ", False, (255, 255, 255))
    end3 = myfont.render("larger than the field", False, (255, 255, 255))
    end4 = myfont.render("Look for the table of", False, (255, 255, 255))
    end5 = myfont.render("contestants in the console", False, (255, 255, 255))
    screen.blit(textsurface,(10,10))
    screen.blit(endsurface, (10,110))
    screen.blit(end2, (10,160))
    screen.blit(end3, (10,210))
    screen.blit(end4, (10,310))
    screen.blit(end5, (10,360))

    if t == 5*FPS:
        finished = True

    pygame.display.update()

pygame.quit()


# reading json file
with open('record.json') as f:
    data = json.load(f)

# asking for a unique name
ok = False
while not ok:
    name = input('Write your name: ')
    if name in data.keys():
        ok = False
        print('This name is already taken')
    else:
        ok = True

# adding info
data[name] = (n, squares[0].worth)

# writing down new info
with open('record.json', 'w') as f:
    json.dump(data, f)

# printing table
print('Table:')
print('Name, Score')
for key in data.keys():
    res, sq_res = map(int, data[key])
    print(key, res)

pygame.quit()
