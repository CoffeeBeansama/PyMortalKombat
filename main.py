import pygame as pg
from settings import *
from player import Player

window = pg.display.set_mode((screenWidth,screenHeight))
pg.display.set_caption("Client")

client = 0

def redrawWindow(player):
    window.fill((255,255,255))
    player.draw(window)
    pg.display.update()

def main():
    run = True
    player = Player(100,100,100,100,(0,255,0))
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                print("this")
                pg.quit()


        player.update()
        redrawWindow(player)

main()