import pygame as pg
from timer import Timer

class Bullet(pg.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.spritePath = "Sprites/Bullets/"
       
        self.poolPos = (-9999,-9999)

        self.sprites = {
            0 : pg.image.load(f"{self.spritePath}1.png").convert_alpha(),
            1 : pg.image.load(f"{self.spritePath}2.png").convert_alpha(),
            2 : pg.image.load(f"{self.spritePath}3.png").convert_alpha(),
            3 : pg.image.load(f"{self.spritePath}4.png").convert_alpha()
        }

        self.image = pg.image.load(f"{self.spritePath}1.png").convert_alpha()

        self.frameIndex = 0

        self.animationTime = 1 / 4

        self.spawned = False

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)

        self.flipped = False

        self.timer = Timer(1500,self.deactivateSelf)
        self.speed = 5

        

    def handleAnimation(self,flipped):
        self.frameIndex += self.animationTime
        if self.frameIndex >= len(self.sprites):
            self.frameIndex = 1
        try:
            self.image = self.sprites.get(int(self.frameIndex))
            if flipped: self.image = pg.transform.flip(self.image, True, False)
        except:
            pass
    
    def activateSelf(self,flipped,pos):
        self.spawned = True
        self.flipped = flipped
        self.hitbox.center = pos
        self.rect.center = pos
        if not self.timer.activated:
            self.timer.activate()

    


    def deactivateSelf(self):
        self.spawned = False
        self.rect.center = self.poolPos

    def handleMovement(self,flipped,speed):
        match flipped:
            case True:
                self.hitbox.centerx += -1 * speed
                self.hitbox.centery += -1 * speed
            case False:
                self.hitbox.centerx += 1 * speed
                self.hitbox.centery += 1 * speed
        self.rect.centerx = self.hitbox.centerx
    
    
    def update(self):
        self.timer.update()
        self.handleAnimation(self.flipped)
        self.handleMovement(self.flipped,self.speed)