from constants import *
import pygame as pg
from person import Fyr
from spokelse import Spokelse
from sau import Sheep
from hindring import Hindring
from pathlib import Path
#from pygame.key import ScancodeWrapper

IMAGE_DIR: Path = Path(__file__).parent




bakgrunnsbilde = pg.image.load(str(IMAGE_DIR / "bilder/bakgrunn.webp"))
        


fyr = Fyr()
spokelse = Spokelse()
spokelser = [spokelse]
sau = Sheep()
sauer = [sau]
hindring = Hindring()
hindringer = [hindring]
pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()


def main():

    
    running = True
    while running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.blit(bakgrunnsbilde,vindu.get_rect())
        
        fyr.draw(vindu)
        fyr.move(keys)
        fyr.update(spokelser,hindringer)

        for spok in spokelser:
            spok.draw(vindu)
            spok.move()
            spok.update()
        
        for s in sauer:
            s.draw(vindu)

        for h in hindringer:
            h.draw(vindu)

        
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()