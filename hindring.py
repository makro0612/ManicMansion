import pygame as pg
from constants import *

from random import randint



class Hindring:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/stone.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (50,50 ))
        self.rect = self.bilde.get_rect()
        self.rect.x = randint(100,VINDU_BREDDE-150)
        self.rect.y = randint(0,VINDU_HOYDE-50)

    def draw(self,vindu:pg.Surface):
        vindu.blit(self.bilde,self.rect)
