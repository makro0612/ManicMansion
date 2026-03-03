from constants import *
import pygame as pg
"""from person import Fyr
from spokelse import Spokelse
from sau import Sheep
from hindring import Hindring
from pathlib import Path
"""

class HoyreSide():
    def __init__(self) -> None:
        self.rect = pg.Rect(VINDU_BREDDE-100, 0,100,VINDU_HOYDE)
    
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu, GREEN,self.rect)

class VenstreSide():
    def __init__(self) -> None:
        self.rect = pg.Rect(0,0,100,VINDU_BREDDE)
    
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu, GREEN,self.rect)
