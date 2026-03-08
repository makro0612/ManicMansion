from constants import *
import pygame as pg
from person import Fyr
from spokelse import Spokelse
from sau import Sheep
from hindring import Hindring
#from pathlib import Path
from safezone import *
#from pygame.key import ScancodeWrapper





#dodBilde = pg.image.load(str(IMAGE_DIR / "bilder/duDodeR.png"))
bakgrunnsbilde = pg.image.load(str(IMAGE_DIR / "bilder/gulv.jpg"))
stortBilde = pg.transform.smoothscale(bakgrunnsbilde, (VINDU_BREDDE, VINDU_HOYDE))
dodBilde = pg.image.load(str(IMAGE_DIR / "bilder/duDode2.jpeg"))
dodBilde = pg.transform.smoothscale(dodBilde,(VINDU_BREDDE,VINDU_HOYDE))
#bakgrunnsbilde = pg.image.load(str(IMAGE_DIR / "bilder/bakgrunn.webp"))
        
dod = False

fyr = Fyr()
spokelse = Spokelse()
spokelser = [spokelse]
sau = Sheep()
sau2 = Sheep()
sauer = [sau,sau2]
hindring = Hindring()
hindringer = [hindring]
pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()
poeng = 0

hoyreside = HoyreSide()
venstreside = VenstreSide()


def main():
    global poeng  # allow incrementing the score from within the function
    # prepare a font for score rendering
    font = pg.font.SysFont(None, 36)


    

    
    running = True
    while running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
                

        vindu.blit(stortBilde,vindu.get_rect())

        venstreside.draw(vindu)
        hoyreside.draw(vindu)
        
        fyr.draw(vindu)
        fyr.move(keys)
        fyr.update(spokelser,hindringer,sauer)

        for spok in spokelser:
            spok.draw(vindu)
            spok.move()
            spok.update()
        
        for s in sauer:
            s.draw(vindu)
            if s.moving:
                # if this is the sheep the player is carrying, position it relative to player
                if s is fyr.attached_sheep:
                    s.rect.x = fyr.rect.x - 25
                    s.rect.y = fyr.rect.y - 50
                else:
                    s.move(keys)
            if s.update(venstreside, hindringer):
                # if this sheep was attached, detach it
                if s is fyr.attached_sheep:
                    fyr.attached_sheep = None
                sauer.remove(s)
                poeng += 1
                nyttSpok = Spokelse()
                spokelser.append(nyttSpok)
                nyHind = Hindring()
                hindringer.append(nyHind)
                
                nySau = Sheep()
                sauer.append(nySau)

        # draw score in top-left corner
        score_surf = font.render(f"Poeng: {poeng}", True, (255, 255, 255))
        vindu.blit(score_surf, (VINDU_BREDDE//2 -18, 10))


        for h in hindringer:
            h.draw(vindu)
        
        if fyr.dod:
            dod_rect = dodBilde.get_rect()
            dod_rect.center = vindu.get_rect().center
            vindu.blit(dodBilde, dod_rect)
            vindu.blit(score_surf, (VINDU_BREDDE//2 -18, 10))

        
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()