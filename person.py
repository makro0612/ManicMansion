import pygame as pg
from pathlib import Path
from pygame.key import ScancodeWrapper

IMAGE_DIR: Path = Path(__file__).parent


class Fyr:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/nekU.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (70, 70))
        self.rect = self.bilde.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed = 5

    def move(self, keys:ScancodeWrapper):
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
    
    #def update(self):


    def draw(self, vindu:pg.Surface):
        vindu.blit(self.bilde, self.rect)
