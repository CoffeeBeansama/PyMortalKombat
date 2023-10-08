import pygame as pg
from settings import *
from level import Level
import sys

class Main:
    def __init__(self):
        pg.init()

        self.gameRunning = True
        self.screen = pg.display.set_mode((screenWidth,screenHeight))
        pg.display.set_caption("Mortal Kombat")
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        while self.gameRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill("black")
            self.level.update()
            pg.display.update()
            self.clock.tick(FPS)


game = Main()
game.run()


