import pygame
from balloon import Balloon

#====CONSTANTS====
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 240
BALL_RADIUS = 24

#====MAIN====
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gameRunning = True


balloon = Balloon(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS)
balloon.force = pygame.Vector2(0, -0.001)

while gameRunning:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.WINDOWSIZECHANGED:
            SCREEN_WIDTH = pygame.display.get_surface().get_size()[0]   
            SCREEN_HEIGHT = pygame.display.get_surface().get_size()[1]  

    # Fill screen with color to wipe away anything from last frame
    screen.fill("white")

    #====MAIN CONTENT====
    balloon.update()


    # Flip the display to put you work on screen
    pygame.display.flip()
    # Limit FPS to 60
    clock.tick(60)
    
pygame.quit()    
