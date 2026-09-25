import pygame

class Bal:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS):
        self.ballRadius = BALL_RADIUS
        self.position = pygame.Vector2(100, 100)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0.01, 0.01)
        self.maxVelocity = 5
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT

    def move(self):
        self.velocityLimit()
        self.velocity += self.acceleration
        self.position += self.velocity


    def collisionDetection(self):
        # Collision detection with wall
        if self.position.x > (self.screenWidth+self.ballRadius) or self.position.x < (0-self.ballRadius):
            self.velocity.x *= -1
            self.acceleration.x *= -1
            
        if self.position.y > (self.screenHeight+self.ballRadius) or self.position.y < (0-self.ballRadius):
            self.velocity.y *= -1
            self.acceleration.y *= -1
  

    def update(self):
        self.move()
        self.collisionDetection()

        print(self.position)


    def velocityLimit(self):
        if abs(self.velocity.x) >= self.maxVelocity:
            if self.velocity.x > 0:
                self.velocity.x = self.maxVelocity
            else:
                self.velocity.x = -self.maxVelocity    
            self.acceleration.x = 0

        if abs(self.velocity.y) >= self.maxVelocity:
            if self.velocity.y > 0:
                self.velocity.y = self.maxVelocity 
            else:
                self.velocity.y = -self.maxVelocity
            self.acceleration.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (150, 150, 150),
                           (int(self.position[0]), int(self.position[1])),
                           self.ballRadius)