import pygame as pg
from pathlib import Path
from pygame.key import ScancodeWrapper
from constants import *
from spokelse import Spokelse

IMAGE_DIR: Path = Path(__file__).parent


class Fyr:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/nekU.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (70, 70))
        self.rect = self.bilde.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed = 5
        self.poeng = 0


    def move(self, keys:ScancodeWrapper):
        if self.rect.y > 0:
            if keys[pg.K_UP]:
                self.rect.y -= self.speed
        else:
            self.rect.y = 0
        
        if self.rect.y + self.rect.height < VINDU_HOYDE:
            if keys[pg.K_DOWN]:
                self.rect.y += self.speed
        else:
            self.rect.y = VINDU_HOYDE - self.rect.height

        if self.rect.x > 0:
            if keys[pg.K_LEFT]:
                self.rect.x -= self.speed
        else:
            self.rect.x = 0
        
        if self.rect.x + self.rect.width < VINDU_BREDDE:
            if keys[pg.K_RIGHT]:
                self.rect.x += self.speed
        else:
            self.rect.x = VINDU_BREDDE - self.rect.width
    
    def reset(self):
        self.poeng = 0
        self.rect.x = 50
        self.rect.y = 50
        
    def update(self,sList:list[Spokelse], hList:list[None]):


    def draw(self, vindu:pg.Surface):
        vindu.blit(self.bilde, self.rect)
