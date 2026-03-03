import pygame as pg
from pathlib import Path
from pygame.key import ScancodeWrapper
from constants import *
from spokelse import Spokelse
from hindring import Hindring
from sau import Sheep
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
        self.dod = False
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        # keep track of the one sheep currently attached to the player (or None)
        self.attached_sheep: Sheep | None = None


    def move(self, keys:ScancodeWrapper):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        # also remember position of attached sheep if any
        if self.attached_sheep is not None:
            self.attached_sheep.prev_x = self.attached_sheep.rect.x
            self.attached_sheep.prev_y = self.attached_sheep.rect.y
        
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
        self.prev_x = 50
        self.prev_y = 50
        self.dod = True
        
    def update(self,sList:list[Spokelse], hList:list[Hindring],saList:list[Sheep]):
        for spok in sList:
            if pg.Rect.colliderect(self.rect, spok):
                self.reset()

        
        for sau in saList:
            if pg.Rect.colliderect(self.rect, sau.rect):
                if self.attached_sheep is None:  # only attach if not carrying a sheep
                    self.attached_sheep = sau
                    sau.moving = True
                    sau.prev_x = sau.rect.x
                    sau.prev_y = sau.rect.y
                # position sheep relative to player (if it's the one we're carrying)
                if self.attached_sheep is sau:
                    sau.rect.y = self.rect.y - 50
                    sau.rect.x = self.rect.x - 25

       
        for hind in hList:
            if pg.Rect.colliderect(self.rect, hind.rect):
                self.rect.x = self.prev_x
                self.rect.y = self.prev_y
                if self.attached_sheep is not None:  # obstacle collisions: rollback both player and attached sheep ( only if picked up)
                    self.attached_sheep.rect.x = self.attached_sheep.prev_x
                    self.attached_sheep.rect.y = self.attached_sheep.prev_y

        


    def draw(self, vindu:pg.Surface):
        vindu.blit(self.bilde, self.rect)
