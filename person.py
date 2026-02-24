<<<<<<< Updated upstream

=======
import pygame as pg
from pathlib import Path

IMAGE_DIR = Path(__file__).parent

class Emo:
    def __init__(self) -> None:
        self.bilde = pg.image.load(IMAGE_DIR / "emo.png")
        self.rect = self.bilde.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed = 5

    def move(self, keys):
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, vindu):
        vindu.blit(self.bilde, self.rect)
>>>>>>> Stashed changes
