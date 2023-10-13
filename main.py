import pygame as pg
from settings import *
from player import Player
from network import Network

window = pg.display.set_mode((screenWidth,screenHeight))
pg.display.set_caption("Client")


def redrawWindow(player,player2):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pg.display.update()

def main():
    run = True
    netWork = Network()

    player1 = netWork.getPlayer()
    clock = pg.time.Clock()

    while run:
        clock.tick(FPS)
        player2 = netWork.send(player1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()


        player1.update()
        player2.update()

        print(f"from player 1: {player1.x}")
        print(f"from player 2:  {player2.x}")
        redrawWindow(player1,player2)


main()