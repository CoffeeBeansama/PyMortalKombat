import pygame as pg
from settings import *
from support import *

class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.speed = 1

        self.rect = (x,y,width,height)

    def draw(self,window):
        pg.draw.rect(window,self.color,self.rect)

    def getInputs(self):
        try:
            keys = pg.key.get_pressed()

            if keys[pg.K_w]:
                self.y -= self.speed


            elif keys[pg.K_s]:
                self.y += self.speed

            elif keys[pg.K_a]:
                self.x -= self.speed

            elif keys[pg.K_d]:
                self.x += self.speed
        except: pass

        self.rect = (self.x,self.y,self.width,self.height)

    def update(self):
        self.getInputs()
