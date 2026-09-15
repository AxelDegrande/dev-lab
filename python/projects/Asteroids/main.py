import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from logger import log_state, log_event
from asteroidField import AsteroidField
from shot import Shot




def main():
    print(f"Starting Astroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen Height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    dt = 0.0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")

        updatable.update(dt)

        for draw in drawable:
            draw.draw(screen)

        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions_with(player):
                log_event("player_hit")
                print("GAME OVER")
                sys.exit()

            for shot in shots:
                if shot.collisions_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()   

        pygame.display.flip()

        dt = clock.tick(60) / 1000


main()