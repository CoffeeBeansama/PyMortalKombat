import pygame as pg
from settings import *
from support import *

class PlayerData:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1

    def getInputs(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        elif keys[pg.K_s]:
            self.y += self.speed
        elif keys[pg.K_a]:
            self.x -= self.speed
        elif keys[pg.K_d]:
            self.x += self.speed

    def getPos(self):
        return self.x,self.y


class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.image = loadSprite(f"Sprites/test/player.png",(50,50)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)


    def update(self,x,y):
        self.rect.center = (x,y)

