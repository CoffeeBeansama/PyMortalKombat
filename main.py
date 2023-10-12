import pygame as pg
from settings import *
from player import Player
from network import Network

window = pg.display.set_mode((screenWidth,screenHeight))
pg.display.set_caption("Client")

client = 0

def readPos(str):
    stringPos = str.split(",")
    return int(stringPos[0]), int(stringPos[1])

def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(player,player2):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pg.display.update()

def main():
    run = True
    netWork = Network()
    startPos = readPos(netWork.getPos())
    player1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
    player2 = Player(0, 0, 100, 100, (0, 255, 0))
    clock = pg.time.Clock()

    while run:
        clock.tick(FPS)
        player2Pos = readPos(netWork.send(makePos((player1.x,player1.y))))
        player2.x = player2Pos[0]
        player2.y = player2Pos[1]
        player2.update()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                print("this")
                pg.quit()


        player1.update()
        redrawWindow(player1,player2)


main()