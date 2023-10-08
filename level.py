import pygame as pg
from settings import *
from player import Player

class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.visibleSprites = pg.sprite.Group()

        self.player = Player((100,200),self.visibleSprites)



    def update(self):
        for sprites in self.visibleSprites:
            self.screen.blit(sprites.image,sprites.pos)
        self.player.update()
