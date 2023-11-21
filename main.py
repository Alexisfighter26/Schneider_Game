import pygame
import time
import sys
from main import utils

# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning make_background.py.')
print('-------------------------------------------\n')

# Create the screen
screen = pygame.display.set_mode((1200, 486))

# Background
background = pygame.image.load("assets/sprites/Min_background.png")

print('Running game...')
running = True
while running:

    # store pygame events in a variable
    events = pygame.event.get()

    # Get events happening in window.
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    screen.blit(background, (0, 0))

    # Update screen based on your game.

# Character intro
    John = player()

    # Show screen to user.
    pygame.display.flip()

pygame.quit()
