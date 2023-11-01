import pygame as pg
from bullets import Bullet

class ObjectPool:
    def __init__(self,visibleSprites,pos=(-999,-999)):
        
        self.pos = pos
        self.visibleSprites = visibleSprites
        self.bullets = {}
        self.index = 0
        self.maximumIndex = 20

        self.data = {}
        for i in range(self.maximumIndex):
            self.data[i] = {}

        self.instantiateBullets()

    def instantiateBullets(self):
        for i in range(self.maximumIndex):
            self.bullets[i] = Bullet(self.pos,self.visibleSprites)

    def createBullets(self,pos,flipped):
        currentBullet = self.bullets[self.index]
        currentBullet.activateSelf(flipped,pos)
        self.index += 1
        if self.index >= len(self.bullets):
            self.index = 0
        return
    
    def handlePlayer2Projectiles(self,data):
        for i in data.keys():
            self.bullets[i].spawned = data[i]["Spawned"]
            self.bullets[i].activateSelf(data[i]["Flipped"],data[i]["Pos"])
            self.bullets[i].handleAnimation(data[i]["Flipped"])


    def update(self):
        for bullets in self.bullets.values():
            if bullets.spawned is True:
                bullets.update()
        
        for i in range(self.maximumIndex):
            self.data[i]["Pos"] = self.bullets[i].rect.center
            self.data[i]["Spawned"] = self.bullets[i].spawned
            self.data[i]["Flipped"] = self.bullets[i].flipped
        