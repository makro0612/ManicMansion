from constants import *
import pygame as pg
from person import *
from pathlib import Path
#from pygame.key import ScancodeWrapper

#IMAGE_DIR: Path = Path(__file__).parent





        


fyr = Fyr()

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

        vindu.fill(WHITE)
        
        fyr.draw(vindu)
        fyr.move(keys)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()