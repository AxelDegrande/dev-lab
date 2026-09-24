import pygame

# Initialize pygame
pygame.init()

# Canvas dimensions
WIDTH = 640
HEIGHT = 240

BALL_RADIUS = 24

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Variables for position and speed of ball
x = 100
y = 100
xspeed = 2.5
yspeed = 2

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill((255, 255, 255))

    # Move the ball according to its speed
    x = x + xspeed
    y = y + yspeed

    # Check for bouncing
    if x > (WIDTH-BALL_RADIUS) or x < (0+BALL_RADIUS):
        xspeed = xspeed * -1

    if y > (HEIGHT-BALL_RADIUS) or y < (0+BALL_RADIUS):
        yspeed = yspeed * -1

    # Draw the ball
    pygame.draw.circle(
        screen,
        (127, 127, 127),  # fill
        (int(x), int(y)), # position
        BALL_RADIUS       # radius
    )

    # Update the display
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

pygame.quit()
