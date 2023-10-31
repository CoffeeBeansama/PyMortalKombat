import pygame as pg
from settings import *
from support import *
from timer import Timer

class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        

        self.spritePath = "Sprites/Player/"

        self.importSprites()
        self.image = pg.image.load(f"Sprites/Player/Idle/player-idle1.png").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)

        self.direction = pg.math.Vector2()

        self.walkingAnimationTime = 1 / 8
        self.attackAnimationTime = 1 / 8
        self.frame_index = 0

        self.state = "Idle"
        self.speed = 1

        self.data = {
            "Pos" : str(self.rect.center),
            "Direction" : str(self.direction)

        }

        self.flipped = True
        self.attacking = False
        self.timer = Timer(200)

    def handleMovement(self, direction):
        self.hitbox.x += direction[0] * self.speed
        self.hitbox.y += direction[1] * self.speed
        self.rect.center = self.hitbox.center

    def importSprites(self):
        self.animationStates = {
            "ShootIdle": [],"ShootWalk": [], "Death": [] , "Idle": [],
            "Roll": [], "Turn Around": [], "Walk": [],
        }

        for animations in self.animationStates.keys():
            fullPath = self.spritePath + animations
            self.animationStates[animations] = import_folder(fullPath)

    def handlePlayer2Movement(self,pos,direction,state,flipped,frameIndex,attacking):
        idle = direction == (0.0,0.0)
        self.flipped = flipped
        if not idle:
            if direction[0] < 0:
                self.state = "Left"
            elif direction[1] < 1:
                self.state = "Up"
        else:
            
            if self.state != "Idle":
                self.state = "Idle"

        self.hitbox.center = pos
        self.rect.center = self.hitbox.center
        self.state = state
        self.frame_index = frameIndex
        self.attacking = attacking
        self.handleAnimation()


    def handleHorizontalDirection(self,x,flipped):
        self.direction.x = x
        self.direction.y = 0
        self.flipped = flipped
        self.state = "Walk" if not self.attacking else "ShootWalk"
        

        
    def handleAnimation(self):
        animation = self.animationStates[self.state]
        self.frame_index += self.walkingAnimationTime if not self.attacking else self.attackAnimationTime

        notMoving = self.direction.x == 0 and self.direction.y == 0
        if self.frame_index >= len(animation):
            if notMoving and self.attacking:
                self.frame_index = len(animation) -1
            else:
                self.frame_index = 0

            
                

        self.image = animation[int(self.frame_index)].convert_alpha()
        self.image =  pg.transform.flip(self.image, True, False) if self.flipped else pg.transform.flip(self.image, False, False)
        self.rect = self.image.get_rect(center=self.hitbox.center)


    def idleState(self):
        if not self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            self.state = "Idle"
        else:
            self.state = "ShootIdle"
            self.direction.x = 0
            self.direction.y = 0

    def handleInputs(self):
        keys = pg.key.get_pressed()
        mousePressed = pg.mouse.get_pressed()


        if keys[pg.K_a]:
            self.handleHorizontalDirection(-1,True)
        elif keys[pg.K_d]:
            self.handleHorizontalDirection(1,False)
        else:
            self.idleState()

        
        if mousePressed[0]:
            self.attackState()
        else:
            self.attacking = False
            

    def attackState(self):
        
        self.attacking = True

    def update(self):

        self.timer.update()
        self.data["Pos"] = self.rect.center
        self.data["Direction"] = (self.direction.x,self.direction.y)
        self.data["Frame Index"] = self.frame_index
        self.data["State"] = self.state
        self.data["Flipped"] = self.flipped
        self.data["Attacking"] = self.attacking
        self.handleInputs()
        self.handleAnimation()
        self.handleMovement(self.direction)
       





