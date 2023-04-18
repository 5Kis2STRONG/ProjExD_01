import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koka_img = pg.image.load("ex01/fig/3.png")
    koka_rev = pg.transform.flip(koka_img, True, False)
    koka_10 = pg.transform.rotozoom(koka_rev, 10, 1.0)
    koka_byousha = [koka_rev, koka_10]

    tmr = 0
    x = 0
    y=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        if x>=1599:
            x=0
        if y>=100:
            y=0
        x+=1
        y+=1
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img,[1600-x,0])
        if y<=49:
            screen.blit(koka_byousha[0], [300, 200])
        if y>=50:
            screen.blit(koka_byousha[1], [300, 200])


        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()