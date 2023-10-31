import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self,pos,groups,flipped):
        super().__init__(groups)

        self.spritePath = "Sprites/Bullets/"
        self.playerFlipped = flipped
        self.image = pg.image.load(f"{self.spritePath}1.png").convert_alpha()

        if self.playerFlipped:
            self.image = pg.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)

        
        self.speed = 2

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
        self.handleMovement(self.playerFlipped,self.speed)