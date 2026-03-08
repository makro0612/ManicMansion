import pygame as pg

#from pygame.key import ScancodeWrapper
from random import randint 
from constants import *




class Spokelse:
    def __init__(self) -> None:
        self.Obilde = pg.image.load(str(IMAGE_DIR / "bilder/ghost.png"))
        self.bilde = pg.transform.smoothscale(self.Obilde, (50, 50))
        self.flipped: pg.Surface = pg.transform.flip(self.bilde, flip_x=True, flip_y=False)
        self.unflipped: pg.Surface = pg.transform.smoothscale(self.Obilde, (50, 50))
        self.rect = self.bilde.get_rect()
        self.rect.x = VINDU_BREDDE//2
        self.rect.y = VINDU_HOYDE//2
        self.speed = 3
        self.direction = randint(1,8)
        

    def move(self):
        if self.direction == 1:
            self.rect.y-=self.speed
        elif self.direction == 2:
            self.rect.y -= self.speed
            self.rect.x += self.speed
            self.bilde = self.flipped
        elif self.direction == 3:
            self.rect.x += self.speed
            self.bilde = self.flipped
        elif self.direction == 4:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.bilde = self.flipped
        elif self.direction == 5:
            self.rect.y += self.speed
        elif self.direction == 6:
            self.rect.y += self.speed
            self.rect.x -= self.speed
            self.bilde = self.unflipped
        elif self.direction == 7:
            self.rect.x -= self.speed
            self.bilde = self.unflipped
        elif self.direction == 8:
            self.rect.x -=self.speed
            self.rect.y -= self.speed
            self.bilde = self.unflipped
    
    def update(self):
        
        if self.rect.x +170 >=VINDU_BREDDE:
            directions:list[int] = [6,7,8]
            self.direction = directions[randint(0,2)]
        elif self.rect.x <=100:
            directions:list[int] = [2,3,4]
            self.direction = directions[randint(0,2)]
        elif self.rect.y <=0:
            directions:list[int] = [4,5,6]
            self.direction = directions[randint(0,2)]
        elif self.rect.y+ 70>=VINDU_HOYDE:
            directions:list[int] = [1,2,8]
            self.direction = directions[randint(0,2)]
          
        

    def draw(self, vindu:pg.Surface):

        vindu.blit(self.bilde, self.rect)
