import pygame
import random
from Player import Player
from utils import *
import time
from Background import *

# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((1200, 486))


# Main Game loop

pygame.init

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = false

# (=====================Character Class======================)

# Copy image to screen

# Update character position



    # Update the player sprite
    player.update()

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the player sprite
    player.draw(window)

    # Update the display




# (=================================================)

# Show screen to user
run = True
while run:
    for event in pygame.event.get():  # Loop through a list of events
        if event.type == pygame.QUIT:  # See if the user clicks the red x
            run = False    # End the loop
            pygame.quit()  # Quit the game
            quit()