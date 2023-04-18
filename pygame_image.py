import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_rev = pg.transform.flip(bg_img, True, False)
    bg_rot = [bg_img, bg_rev]
    koka_img = pg.image.load("ex01/fig/3.png")
    koka_rev = pg.transform.flip(koka_img, True, False)
    koka_25 = pg.transform.rotozoom(koka_rev, 2.5, 1.0)
    koka_50 = pg.transform.rotozoom(koka_rev, 5.0, 1.0)
    koka_10 = pg.transform.rotozoom(koka_rev, 10, 1.0)
    koka_byousha = [koka_rev, koka_25, koka_50, koka_10, koka_50, koka_25]

    tmr = 0
    x = 0
    y=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        if y>=120:
            y=0
        if x>=3199:
            x=0
        x+=1
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_rev,[1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        if y<=19:
            screen.blit(koka_byousha[0], [300, 200])
        elif y<=39:
            screen.blit(koka_byousha[1], [300, 200])
        elif y<=59:
            screen.blit(koka_byousha[2], [300, 200])
        elif y<=79:
            screen.blit(koka_byousha[3], [300, 200])
        elif y<=99:
            screen.blit(koka_byousha[4], [300, 200])
        elif y>=100:
            screen.blit(koka_byousha[5], [300, 200])


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()