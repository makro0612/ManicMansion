import pygame as pg
from pathlib import Path
#from pygame.key import ScancodeWrapper
from random import randint 
from constants import *

IMAGE_DIR: Path = Path(__file__).parent


class Spokelse:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/ghost.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (70, 70))
        self.rect = self.bilde.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed = 5
        self.direction = randint(1,8)
        

    def move(self):
        if self.direction == 1:
            self.rect.y-=self.speed
        elif self.direction == 2:
            self.rect.y -= self.speed
            self.rect.x += self.speed
        elif self.direction == 3:
            self.rect.x += self.speed
        elif self.direction == 4:
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.direction == 5:
            self.rect.y += self.speed
        elif self.direction == 6:
            self.rect.y += self.speed
            self.rect.x -= self.speed
        elif self.direction == 7:
            self.rect.x -= self.speed
        elif self.direction == 8:
            self.rect.x -=self.speed
            self.rect.y -= self.speed
    
    def update(self):
        
        if self.rect.x +70 >=VINDU_BREDDE:
            directions:list[int] = [6,7,8]
            self.direction = directions[randint(0,2)]
        elif self.rect.x <=0:
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
