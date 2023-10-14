import pygame as pg
from settings import *
from playerdata import *
from network import Network
from level import Level


class Game:
    def __init__(self):
        self.window = pg.display.set_mode((screenWidth,screenHeight))
        pg.display.set_caption("PyMortalKombat")
        self.running = True
        self.level = Level()
        self.clock = pg.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

            self.level.update()



game = Game()
game.run()