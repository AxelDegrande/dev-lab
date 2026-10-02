import pygame
import random
import math

class Balloon:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS):
        self.screen = screen
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT
        self.ballRadius = BALL_RADIUS
        self.position = pygame.Vector2(random.random()*self.screenWidth, self.screenHeight-self.ballRadius) # Random start position in the X range, Y starts at bottom of screen
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.force = pygame.Vector2(0, 0) # Force applied in x, y 
        self.mass = 0.1*math.pi*self.ballRadius**2 # Mass of the object is defined by the area of the cicle
        self.maxVelocity = 2
        self.maxAcceleration = 0.1
        
    def draw(self):
        pygame.draw.circle(self.screen, color='red', center=self.position, radius=self.ballRadius)

    def move(self):
        self.acceleration += self.force / self.mass
        self.accelerationLimit()
        self.velocity += self.acceleration
        self.velocityLimit()
        self.position += self.velocity

    def velocityLimit(self):
        self.velocity.x = max(-self.maxVelocity, min(self.velocity.x, self.maxVelocity))
        self.velocity.y = max(-self.maxVelocity, min(self.velocity.y, self.maxVelocity))

    def accelerationLimit(self):
         self.acceleration.x = max(-self.maxAcceleration, min(self.acceleration.x, self.maxAcceleration))
         self.acceleration.y = max(-self.maxAcceleration, min(self.acceleration.y, self.maxAcceleration))

    def collisionDetection(self):
        if self.position.x > (self.screenWidth-self.ballRadius) or self.position.x < (0+self.ballRadius):
            self.velocity.x *= -1

        if self.position.y > (self.screenHeight-self.ballRadius) or self.position.y < (0+self.ballRadius):  
            self.position.y = self.ballRadius # Place bal on the edge of the border, otherwise it starts glitching
            self.velocity.y *= -1
   

    def update(self):
        self.draw()
        self.move()
        self.collisionDetection()            