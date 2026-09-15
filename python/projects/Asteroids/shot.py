import pygame
from circleShape import CircleShape
import constants


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)


    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.move(dt)

    def move(self,dt):
        self.position = self.position + (self.velocity * dt)  