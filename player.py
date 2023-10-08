import pygame as pg
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.pos = pos
        self.image = loadSprite("Sprites/Player/Idle/00.png",(350,250)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)


    def importSprites(self):
        spritePath = "Sprites/Player/"
        self.animations = { "idle": []}

    def getInputs(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.image = pg.transform.flip(self.image, True, False).convert_alpha()


        elif keys[pg.K_d]:
            self.image = pg.transform.flip(self.image, False, False).convert_alpha()

    def update(self):
        self.getInputs()