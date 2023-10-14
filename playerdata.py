import pygame as pg
from settings import *
from support import *

class PlayerData:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
        self.frameIndex = 0
        self.animationTIme = 1 / 25


    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        elif keys[pg.K_s]:
            self.y += self.speed
        elif keys[pg.K_a]:
            self.x -= self.speed
        elif keys[pg.K_d]:
            self.x += self.speed

        self.frameIndex += self.animationTIme

        if self.frameIndex >= 10:
            self.frameIndex = 0

    def getPos(self):
        return self.x,self.y

class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.image = loadSprite(f"Sprites/test/player.png",(400,250)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)

        self.animationTIme = 1 / 8
        self.state = "Idle"
        self.importSprites()

    def importSprites(self):
        player_path = "Sprites/Player/"
        self.animations_States = {
            "Idle": []
        }

        for animation in self.animations_States.keys():
            full_path = player_path + animation
            self.animations_States[animation] = import_folder(full_path)

    def animate(self,frameIndex):
        animation = self.animations_States[self.state]

        self.image = pg.transform.scale(animation[int(frameIndex)],(400,250)).convert_alpha()
        self.rect = self.image.get_rect(center=self.hitbox.center)


    def update(self,x,y,frameIndex):
        self.animate(frameIndex)
        self.rect.center = (x,y)

