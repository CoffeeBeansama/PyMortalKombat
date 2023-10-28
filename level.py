import pygame as pg
from player import Player
from network import Network
import ast

#region Camera
class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_canvas = pg.display.get_surface()
        self.half_width = self.display_canvas.get_size()[0] // 2
        self.half_height = self.display_canvas.get_size()[1] // 2


        self.internalSurfaceSize = (500, 500)
        self.internalSurface = pg.Surface(self.internalSurfaceSize, pg.SRCALPHA)
        self.internalRect = self.internalSurface.get_rect(center=(self.half_width, self.half_height))
        self.offset_rect = None
        self.zoomInSize = (1100, 1100)

        self.internalOffset = pg.math.Vector2()
        self.internalOffset.x = self.internalSurfaceSize[0] // 2 - self.half_width
        self.internalOffset.y = self.internalSurfaceSize[1] // 2 - self.half_height

        self.offset = pg.math.Vector2()

        

    def custom_draw(self, player):
        # getting the offset  for camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        self.internalSurface.fill("black")


        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.offset_rect = sprite.rect.topleft - self.offset + self.internalOffset

            self.internalSurface.blit(sprite.image, self.offset_rect)


        scaledSurface = pg.transform.scale(self.internalSurface, self.zoomInSize)
        scaledRect = scaledSurface.get_rect(center=(self.half_width, self.half_height))
        self.display_canvas.blit(scaledSurface, scaledRect)

#endregion


class Level:
    def __init__(self):
        self.screen = pg.display.get_surface()

        self.network = Network()

        try:
            self.playerID = int(self.network.getPlayerID())
        except:
            pass

        self.visibleSprites = CameraGroup()

        p1Pos = (100,100)
        p2Pos = (150,100)

        self.player = Player(p1Pos if self.playerID == 0  else p2Pos,self.visibleSprites)
        self.player2 = Player(p2Pos if self.playerID == 0 else p1Pos,self.visibleSprites)

        self.gameData = {
             "Player" : self.player.data
        }

    def update(self):
        self.game = self.network.send("get")
    
        self.player.update()
        self.gameData["Player"] = self.player.data

        self.network.send(str(self.gameData))

        self.visibleSprites.custom_draw(self.player)
        
        try:
            match self.playerID:
                case 0:
                        
                        data = ast.literal_eval(str(self.game.getPlayerTwoData()))
                        self.player2.handlePlayer2Movement(data["Player"]["Pos"],data["Player"]["Direction"])
                case 1:
                        
                        data = ast.literal_eval(str(self.game.getPlayerOneData()))
                        self.player2.handlePlayer2Movement(data["Player"]["Pos"],data["Player"]["Direction"])
        except:
             return     
                  
        
        
        
        