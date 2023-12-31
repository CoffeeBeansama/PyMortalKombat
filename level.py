import pygame as pg
from player import Player
from network import Network
from support import loadSprite
from settings import screenWidth,screenHeight
import ast
from timer import Timer
from pool import ObjectPool

#region Camera
class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_canvas = pg.display.get_surface()
        self.half_width = self.display_canvas.get_size()[0] // 2
        self.half_height = self.display_canvas.get_size()[1] // 2

        self.backgroundSprite = loadSprite("Sprites/Background.png",(500,300))

        self.backgroundRect = self.backgroundSprite.get_rect(topleft=(0,0))

        self.internalSurfaceSize = (400, 500)
        self.internalSurface = pg.Surface(self.internalSurfaceSize, pg.SRCALPHA)
        self.internalRect = self.internalSurface.get_rect(center=(self.half_width, self.half_height))
        self.offset_rect = None
        self.zoomInSize = (800, 750)

        self.internalOffset = pg.math.Vector2()
        self.internalOffset.x = self.internalSurfaceSize[0] // 2 - self.half_width
        self.internalOffset.y = self.internalSurfaceSize[1] // 2 - self.half_height

        self.offset = pg.math.Vector2()

        

    def custom_draw(self, player):
        # getting the offset  for camera
        self.offset.x = 250 - self.half_width
        self.offset.y = 180 - self.half_height

        self.internalSurface.fill("black")
        backgroundPos = self.backgroundRect.topleft - self.offset + self.internalOffset
        self.internalSurface.blit(self.backgroundSprite.convert_alpha(),backgroundPos)

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
        pg.font.init()
        self.network = Network()

        try:
            self.playerID = int(self.network.getPlayerID())
        except:
            pass

        self.visibleSprites = CameraGroup()
        self.font = pg.font.Font("font/DeterminationMonoWebRegular-Z5oq.ttf",18)

        p1Pos = (250,225)
        p2Pos = (270,225)

        self.player = Player(p1Pos if self.playerID == 0  else p2Pos,self.visibleSprites,self.createPlayerBullets)
        self.player2 = Player(p2Pos if self.playerID == 0 else p1Pos,self.visibleSprites,self.createPlayerBullets)

        self.gameData = {
             "Player" : self.player.data
        }

        self.bullets = []
        self.timer = Timer(200)
        
        self.player1ObjectPool = ObjectPool(self.visibleSprites)
        self.player2ObjectPool = ObjectPool(self.visibleSprites)


    def createPlayerBullets(self):
        player = self.player
        if not self.timer.activated:
            bulletStartx = player.rect.centerx - 15 if player.flipped else  player.rect.centerx + 15
            bulletStarty = player.rect.centery 
            self.player1ObjectPool.createBullets((bulletStartx,bulletStarty),self.player.flipped)
            self.timer.activate()


    def displayFPS(self,clock):
         fps = self.font.render(f"FPS:{round(clock.get_fps())}",True,(255,255,255))
         pos = (730,10)
         self.screen.blit(fps,pos)

    def update(self):
        self.timer.update()
        self.game = self.network.send("get")

        self.player.update()
        self.player1ObjectPool.update()
        self.gameData["Player"] = self.player.data
        self.gameData["Bullets"] = self.player1ObjectPool.data
        
        self.network.send(str(self.gameData))

        
        self.visibleSprites.custom_draw(self.player)
 
        try:
            match self.playerID:
                case 0:
                        if type(self.game.getPlayerTwoData()) == str:
                            data = ast.literal_eval(str(self.game.getPlayerTwoData()))
                            playerData = data["Player"]
                            bulletData = data["Bullets"]
                           
                            self.player2ObjectPool.handlePlayer2Projectiles(bulletData)
                            self.player2.handlePlayer2Movement(playerData["Pos"],playerData["Direction"],playerData["State"],playerData["Flipped"],playerData["Frame Index"],playerData["Attacking"])
                       
                case 1:
                        if type(self.game.getPlayerOneData()) == str:
                            data = ast.literal_eval(str(self.game.getPlayerOneData()))
                            playerData = data["Player"]
                            bulletData = data["Bullets"]
                            
                            self.player2ObjectPool.handlePlayer2Projectiles(bulletData)
                           
                            self.player2.handlePlayer2Movement(playerData["Pos"],playerData["Direction"],playerData["State"],playerData["Flipped"],playerData["Frame Index"],playerData["Attacking"])
        except:
            pass
                  
        
        
        
        