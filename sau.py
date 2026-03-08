import pygame as pg

from pygame.key import ScancodeWrapper
from constants import *
from random import randint
from safezone import VenstreSide
from hindring import Hindring




class Sheep:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/sheepU.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (70, 70))
        self.rect = self.bilde.get_rect()
        self.rect.x = VINDU_BREDDE - 70
        self.rect.y = randint(0,VINDU_HOYDE-70)
        self.speed = 5
        self.moving = False
        # store previous position for collision handling
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

    def move(self, keys:ScancodeWrapper):
        # track previous position
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
    
    def update(self, venstreside:VenstreSide, hList:list[Hindring]) -> bool:
        
        for hind in hList:
            if pg.Rect.colliderect(self.rect, hind.rect):
                self.rect.x = self.prev_x
                self.rect.y = self.prev_y

        if pg.Rect.colliderect(self.rect, venstreside.rect):
            return True
        return False




    def draw(self, vindu:pg.Surface):
        vindu.blit(self.bilde, self.rect)
