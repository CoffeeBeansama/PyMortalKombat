import pygame as pg
from bullets import Bullet

class ObjectPool:
    def __init__(self,visibleSprites,pos=(-999,-999)):
        
        self.pos = pos
        self.visibleSprites = visibleSprites
        self.bullets = []
        self.index = 0
        self.maximumIndex = 20

        self.instantiateBullets()

    def instantiateBullets(self):
        for i in range(self.maximumIndex):
            self.bullets.append(Bullet(self.pos,self.visibleSprites))

    def createBullets(self,pos,flipped):
        currentBullet = self.bullets[self.index]
        currentBullet.activateSelf(flipped,pos)
        self.index += 1
        if self.index >= len(self.bullets):
            self.index = 0
        return
    
    def update(self):
        for bullets in self.bullets:
            if bullets.spawned is True:
                bullets.update()