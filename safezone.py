from constants import *
import pygame as pg
"""from person import Fyr
from spokelse import Spokelse
from sau import Sheep
from hindring import Hindring
from pathlib import Path"""





class HoyreSide():
    def __init__(self) -> None:
        self.rect = pg.Rect(VINDU_BREDDE-100, 0,100,VINDU_HOYDE)
    
    def draw(self,vindu:pg.Surface):
        bilde = pg.image.load(str(IMAGE_DIR / "bilder/grass.jpg"))
        stortBilde = pg.transform.smoothscale(bilde, (100, VINDU_HOYDE))

        vindu.blit(stortBilde,self.rect)

class VenstreSide():
    def __init__(self) -> None:
        self.rect = pg.Rect(0,0,100,VINDU_HOYDE)
    
    def draw(self,vindu:pg.Surface):
        bilde = pg.image.load(str(IMAGE_DIR / "bilder/grass.jpg"))
        stortBilde = pg.transform.smoothscale(bilde, (100, VINDU_HOYDE))

        vindu.blit(stortBilde,self.rect)
