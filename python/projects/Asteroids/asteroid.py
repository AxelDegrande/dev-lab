import pygame
import random
from circleShape import CircleShape
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.move(dt)

    def move(self,dt):
        self.position = self.position + (self.velocity * dt)      


    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        left_velocity = self.velocity.rotate(angle)
        right_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        first_asteroid_split = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid_split.velocity = left_velocity * 1.2
        second_asteroid_split = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid_split.velocity = right_velocity * 1.2  