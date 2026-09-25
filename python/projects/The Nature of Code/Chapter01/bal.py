import pygame

class Bal:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS):
        self.ballRadius = BALL_RADIUS
        self.position = pygame.Vector2(100, 100)
        self.velocity = pygame.Vector2(2, 2)
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT

    def move(self):
        self.position += self.velocity

    def collisionDetection(self):
        # Collision detection with wall
        if self.position[0] > (self.screenWidth-self.ballRadius) or self.position[0] < (0+self.ballRadius):
            self.velocity[0] *= -1
        if self.position[1] > (self.screenHeight-self.ballRadius) or self.position[1] < (0+self.ballRadius):
            self.velocity[1] *= -1
  

    def update(self):
        self.move()
        self.collisionDetection()

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (150, 150, 150),
                           (int(self.position[0]), int(self.position[1])),
                           self.ballRadius)