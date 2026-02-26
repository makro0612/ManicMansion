import pygame as pg
from constants import *
from pathlib import Path

IMAGE_DIR: Path = Path(__file__).parent

class Hindring:
    def __init__(self) -> None:
        self.bilde = pg.image.load(str(IMAGE_DIR / "bilder/stone.png"))
        self.bilde = pg.transform.smoothscale(self.bilde, (100, 100))
        self.rect = self.bilde.get_rect()
        self.rect.x = 75
        self.rect.y = 75
