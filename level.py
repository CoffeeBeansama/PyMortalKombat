import pygame as pg
from settings import *
from playerdata import *
from network import Network

class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.visibleSprites = pg.sprite.Group()
        self.netWork = Network()
        self.player1Data = self.netWork.getPlayer()

        self.player1 = Player((0,0),[self.visibleSprites])
        self.player2 = Player((600,0),[self.visibleSprites])


    def redrawWindow(self,player1, player2):
        self.screen.fill((0, 0, 0))
        for sprites in self.visibleSprites:
            self.screen.blit(sprites.image,sprites.rect.center)
        pg.display.update()


    def update(self):
        self.player2Data = self.netWork.send(self.player1Data)

        self.player1Data.update()
        self.player2Data.update()

        self.player1.update(self.player1Data.getPos()[0],self.player1Data.getPos()[1],self.player1Data.frameIndex)
        self.player2.update(self.player2Data.getPos()[0],self.player2Data.getPos()[1],self.player2Data.frameIndex)

        self.redrawWindow(self.player1,self.player2)