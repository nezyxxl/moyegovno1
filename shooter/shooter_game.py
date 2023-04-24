#Створи власний Шутер!

from pygame import *
import random

font.init()

window = display.set_mode((700,500))
background = transform.scale(image.load("galaxy.jpg"),(700,500))
window.blit(background,(0,0))

finish = False

FPS = 60
clock = time.Clock()

win = 0

hp = 3

game = True

font2 = font.SysFont('Impact',70)

mixer.init()
mixer.music.load('space.ogg')
#mixer.music.play()
fireq = mixer.Sound('fire.ogg')

lost = 0 
killed = 0

bullets = sprite.Group()
            

class GameSprite(sprite.Sprite):
    def __init__(self, imag, rect_h, rect_w, speed, x, y):
        super().__init__()
        self.rect_h = rect_h
        self.rect_w = rect_w
        self.image = transform.scale(image.load(imag), (self.rect_h, self.rect_w))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 70:
            self.kill()
            
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x>5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x<600:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",20,15,4,self.rect.centerx,self.rect.top)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 600:
            self.rect.x = random.randint(0, 750)
            self.rect.y = 0
            lost = lost + 1
            text_lose = font2.render("Пропущено:" + str(lost),1,(255,255,255))




bullets = sprite.Group()



enem133 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)
enem143 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)
enem123 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)
enem122 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)
enem111 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)

rocket = Player("rocket.png", 100,100,10,0,400)
monsters = sprite.Group()
monsters.add(enem123)
monsters.add(enem122)
monsters.add(enem111)


while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:    
            if e.key == K_SPACE:
                fireq.play()
                rocket.fire()
    text_losee = font2.render("Ви програли!",1,(225, 0, 0))
    text_winn = font2.render("Ви перемогли!",1,(12, 167, 1))
    if lost >= 3:
        window.blit(text_losee,(135,170))
        finish = True
    if win >= 10:
        window.blit(text_winn,(135,170))
        finish = True         

    if finish != True:
        text_lose = font2.render("Пропущено:" + str(lost),1,(255,255,255))
        window.blit(text_lose,(5,5))
        key_pressed = key.get_pressed()

        sprites_list2 = sprite.spritecollide(rocket,monsters,False)
        sprites_list1 = sprite.groupcollide(monsters,bullets,True,True)
        for monster in sprites_list1:
            win = win + 1
            enem133 = Enemy("ufo.png",75,75,random.randint(1,4),random.randint(0,500),0)
            monsters.add(enem133)



        text_win = font2.render("Збито:" + str(win),1,(255,255,255))
        window.blit(text_win,(10,75))
        bullets.draw(window)       
        rocket.update()
        rocket.reset()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
    clock.tick(FPS)
    display.update()

        


