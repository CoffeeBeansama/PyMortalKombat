import pygame as pg
from settings import *
from level import Level


class Game:
    def __init__(self):
        self.window = pg.display.set_mode((screenWidth,screenHeight))
        
        self.running = True
        self.level = Level()
        pg.display.set_caption(str(self.level.playerID+1))
        self.clock = pg.time.Clock()

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

            self.window.fill("black")
            self.level.update()
            pg.display.update()
            self.clock.tick(FPS)

game = Game()
game.run()