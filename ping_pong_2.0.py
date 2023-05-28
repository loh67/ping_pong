from pygame import*
from random import randint
from time import time as timer
from time import sleep
font.init()

class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, player_height, player_weight):
        super().__init__()
        self.player_height = player_height
        self.player_weight = player_weight
        self.image = transform.scale(image.load(player_image), (self.player_height, self.player_weight))
        self.player_speed_x = player_speed_x
        self.player_speed_y = player_speed_y
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(gameSprite):
    def update_first(self):
        pressed = key.get_pressed()
        if pressed [K_w] and self.rect.y > 0:
            self.rect.y -= self.player_speed_y
        if pressed [K_s] and self.rect.y < 650:
            self.rect.y += self.player_speed_y


    def update_second(self):
        pressed = key.get_pressed()
        if pressed [K_UP] and self.rect.y > 0:
            self.rect.y -= self.player_speed_y
        if pressed [K_DOWN] and self.rect.y < 650:
            self.rect.y += self.player_speed_y

class Ball(gameSprite):
    def update(self):
        self.rect.x += self.player_speed_x
        self.rect.y += self.player_speed_y
        if sprite.collide_rect(player_first, ball):
            self.player_speed_x *= -1
        if sprite.collide_rect(player_second, ball):
            self.player_speed_x *= -1
        if self.rect.y >= 750:
            self.player_speed_y *= -1
        if self.rect.y <= 0:
            self.player_speed_y *= -1




mw = display.set_mode((1000, 800))
display.set_caption('Ping-pong')
back = transform.scale(image.load('back_1.jpg'), (1000, 800))
FPS = 150
game = True
finish = False



#создание надписей победы
font.init()
font = font.SysFont('Arial', 70)

font_1 = font.render('Красный победил!', True, (255, 0, 0))
font_2 = font.render('Синий победил!', True, (0, 0, 255))

#Создание спрайтов
player_first = Player('platform1.png', 50, 400, 0, 5, 45, 150)
player_second = Player('platform2.png', 900, 400, 0, 5, 45, 150)
ball = Ball('ball.png', 500, 400, 3, 3, 50, 50)







platforms = sprite.Group()
platforms.add(player_first, player_second)

while game:
    mw.blit(back, (0, 0))
    platforms.draw(mw)
    ball.reset()

    if finish != True :
        player_first.update_first()
        player_second.update_second()
        ball.update()




    for a in event.get():
        if a.type == QUIT:
            game = False

    if ball.rect.x <= 0:
        finish = True  
        mw.blit(font_2, (230,200))      
    if ball.rect.x >= 950:
        finish = True 
        mw.blit(font_1, (200,200))

    clock = time.Clock()
    clock.tick(FPS)
    display.update()