import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koka_img = pg.image.load("ex01/fig/3.png")
    kokat_rev = pg.transform.flip(koka_img, True, False)
    kokat_10 = pg.transform.rotozoom(koka_img, 10, 1.0)
    kokat_byousha = [kokat_rev, kokat_10]

    tmr = 0
    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        if x>=1599:
            x=0
        x+=1
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img,[1600-x,0])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()