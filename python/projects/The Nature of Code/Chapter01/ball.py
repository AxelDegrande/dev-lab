import pygame
import random
import numpy as np

class Ball:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, modeColission=1, modeAcceleration=1):
        self.ballRadius = BALL_RADIUS
        self.position = pygame.Vector2(100, 100)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0.01, -0.01)
        self.maxVelocity = 2
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT
        self.modeColission = modeColission # mode 1: ball bounces off walls, mode 2: ball travels across the screen
        self.modeAcceleration = modeAcceleration # mode 1: normal mode, mode 2: random acceleration, mode 3: follow mouse
        self.mousePos = np.array(pygame.mouse.get_pos())

    def move(self):
        self.velocityLimit()
        self.velocity += self.acceleration
        self.position += self.velocity

        match self.modeAcceleration:
            case 1:
                pass

            case 2:
                self.acceleration = pygame.Vector2(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))

            case 3:
                self.mousePos = np.array(pygame.mouse.get_pos()) # Get mouse position (x, y)
                ballPos = np.array(self.position) # Get ball position (x, y)
                direction = np.subtract(self.mousePos, ballPos) # Get the direction between mouse and ball (dx, dy)
                if np.linalg.norm(direction) > 0: # Get the magnitude of the direction and if it is higher then 0 get the norm
                    directionNorm = np.divide(direction, np.linalg.norm(direction)) # Norm is array devided by the magnitude
                
                self.acceleration = pygame.Vector2(directionNorm[0] * 0.2, directionNorm[1] * 0.2)   

            
    def collisionDetection(self):
        match self.modeColission:
            case 1: # Collision detection with wall
                if self.position.x > (self.screenWidth-self.ballRadius) or self.position.x < (0+self.ballRadius):
                    self.velocity.x *= -1
                    self.acceleration.x *= -1

                if self.position.y > (self.screenHeight-self.ballRadius) or self.position.y < (0+self.ballRadius):    
                    self.velocity.y *= -1
                    self.acceleration.y *= -1    

            case 2: # No collision, ball moves from one side too the other side.   :
                if self.position.x > (self.screenWidth+self.ballRadius):
                    self.position.x = 0
    
                if self.position.x < (0-self.ballRadius):
                    self.position.x = self.screenWidth

                if self.position.y > (self.screenHeight+self.ballRadius):
                    self.position.y = 0
    
                elif self.position.y < (0-self.ballRadius):
                    self.position.y = self.screenHeight         


    def update(self):
        self.move()
        self.collisionDetection()


    def velocityLimit(self):
        if abs(self.velocity.x) > self.maxVelocity:
            if self.velocity.x > 0:
                self.velocity.x = self.maxVelocity
            else:
                self.velocity.x = -self.maxVelocity    

        if abs(self.velocity.y) > self.maxVelocity:
            if self.velocity.y > 0:
                self.velocity.y = self.maxVelocity 
            else:
                self.velocity.y = -self.maxVelocity


    def draw(self, screen):
        pygame.draw.circle(screen,
                           (150, 150, 150),
                           (int(self.position[0]), int(self.position[1])),
                           self.ballRadius)