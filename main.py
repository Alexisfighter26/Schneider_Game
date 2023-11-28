from Player import *
import sys


# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((1200, 486))

# Background
background = pygame.image.load("assets/sprites/Min_background.png")

# Creating Instance of Player
player = Player()

print('Running game...')
running = True
while running:
    # store pygame events in a variable
    # events = pygame.event.get()
    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Player Position
    player.update_plyr_position()

    # Draw background.
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

    # Drawing player
    player.draw_plyr(screen)

    # Flip screen so user can see it
    pygame.display.flip()

    # Slow loop to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
