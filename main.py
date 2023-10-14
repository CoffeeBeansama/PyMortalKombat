import pygame as pg
from settings import *
from player import Player
from network import Network
from level import Level

window = pg.display.set_mode((screenWidth,screenHeight))
pg.display.set_caption("Client")

def main():
    run = True
    level = Level()
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()

        level.update()




main()