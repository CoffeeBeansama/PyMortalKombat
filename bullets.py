import pygame as pg
from timer import Timer

class Bullet(pg.sprite.Sprite):
    def __init__(self,pos,groups,flipped):
        super().__init__(groups)

        self.spritePath = "Sprites/Bullets/"
        self.playerFlipped = flipped

        self.sprites = {
            0 : pg.image.load(f"{self.spritePath}1.png").convert_alpha(),
            1 : pg.image.load(f"{self.spritePath}2.png").convert_alpha(),
            2 : pg.image.load(f"{self.spritePath}3.png").convert_alpha(),
            3 : pg.image.load(f"{self.spritePath}4.png").convert_alpha()
        }

        self.image = pg.image.load(f"{self.spritePath}1.png").convert_alpha()

        self.frameIndex = 0

        self.animationTime = 1 / 4

        if self.playerFlipped:
            self.image = pg.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)

        self.timer = Timer(1500,self.kill)
        self.speed = 5

        if not self.timer.activated:
            self.timer.activate()

    def handleAnimation(self,flipped):
        self.frameIndex += self.animationTime

        if self.frameIndex >= len(self.sprites):
            self.frameIndex = 1

        try:
            self.image = self.sprites.get(int(self.frameIndex))
            if flipped: self.image = pg.transform.flip(self.image, True, False)
 
        except:
            pass
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
        self.handleAnimation(self.playerFlipped)
        self.handleMovement(self.playerFlipped,self.speed)