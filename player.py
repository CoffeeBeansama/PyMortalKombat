import pygame as pg
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.pos = pos
        self.image = pg.Surface((10, 10))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)


    def importSprites(self):
        spritePath = "Sprites/Player/"
        self.animations = { "idle": []}

    def getInputs(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            print("left")
        elif keys[pg.K_d]:
            print("right")

    def update(self):
        self.getInputs()