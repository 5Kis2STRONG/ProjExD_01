import pygame as pg

def main():
    screen = pg.display.set_mode((1600,900))
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koka_img = pg.image.load("ex01/fig/3.png")
    kokat_rev = pg.transform.flip(koka_img, True, False)
    kokat_10 = pg.transform.rotozoom(koka_img, 10, 1.0)
    kokat_byousha = [kokat_rev, kokat_10]
