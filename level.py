import pygame as pg
from settings import *
from player import Player
from network import Network

class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.visibleSprites = pg.sprite.Group()
        self.netWork = Network()
        self.player1 = self.netWork.getPlayer()

    def redrawWindow(self,player, player2):
        try:
            self.screen.fill((255, 255, 255))
            player.draw(self.screen)
            player2.draw(self.screen)
            pg.display.update()
        except:
            pass

    def update(self):
        for sprites in self.visibleSprites:
            self.screen.blit(sprites.image,sprites.pos)

        self.player2 = self.netWork.send(self.player1)
        self.player1.update()
        self.player2.update()
        self.redrawWindow(self.player1,self.player2)