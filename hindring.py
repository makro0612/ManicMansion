import pygame as pg
from constants import *
from pathlib import Path
from random import randint

IMAGE_DIR: Path = Path(__file__).parent

class Hindring:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/stone.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (50,50 ))
        self.rect = self.bilde.get_rect()
        self.rect.x = randint(0,VINDU_BREDDE-50)
        self.rect.y = randint(0,VINDU_HOYDE-50)

    def draw(self,vindu:pg.Surface):
        vindu.blit(self.bilde,self.rect)
