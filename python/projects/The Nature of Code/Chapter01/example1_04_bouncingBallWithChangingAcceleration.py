import pygame
from balChangingAcceleration import Bal

# ====CONSTANTS====
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 240
BALL_RADIUS = 24
# ====VARIABLES====



# ====MAIN====
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()
running = True

bal = Bal(SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS)

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.WINDOWSIZECHANGED:
            SCREEN_WIDTH = pygame.display.get_surface().get_size()[0]
            SCREEN_HEIGHT = pygame.display.get_surface().get_size()[1]
            bal.screenWidth = SCREEN_WIDTH
            bal.screenHeight = SCREEN_HEIGHT
    

    # Fill screen with color to wipe away anything from last frame
    screen.fill("white")

    bal.update()
    bal.draw(screen)
    
    # Flip the display to put you work on screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()    

