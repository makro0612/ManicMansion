from constants import *
import pygame as pg
from person import *



        


fyr = Fyr()

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()


def main():

    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        vindu.fill(WHITE)
        
        fyr.draw(vindu)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()