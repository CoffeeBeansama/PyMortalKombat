import pygame as pg
from settings import *
from player import Player
from network import Network

class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.visibleSprites = pg.sprite.Group()
        self.netWork = Network()
        self.player1Data = self.netWork.getPlayer()

    def redrawWindow(self,player1, player2):
        self.screen.fill((255, 255, 255))
        print(f"from player1: {player1}")
        print(f"from player2: {player2}")
        pg.display.update()


    def update(self):
        for sprites in self.visibleSprites:
            self.screen.blit(sprites.image,sprites.pos)

        self.player2Data = self.netWork.send(self.player1Data)
        self.redrawWindow(self.player1Data,self.player2Data)