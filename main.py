import sys
from pygame import mixer
from Player import Player
from Enemies import Enemy
import pygame


# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((1200, 486))

# Defining screen dimensions (easier to set bounds for character)
screen_width = 1200
screen_height = 486

# Background
background = pygame.image.load("assets/sprites/Min_background.png")

# Background Sound!
mixer.init()
mixer.music.load("assets/sound/backgroundmusic.ogg")
mixer.music.play()

# Creating Instance of Player
player = Player()

# Create gruop Instance of Enemy
enemy_group = pygame.sprite.Group()
# The instance of enemies
enemy1 = Enemy()
# Creating an instance of Enemy and adding it to the enemy_group
enemy_group.add(enemy1)


# Main Game loop
print('Running game...')
running = True
while running:
    # store pygame events in a variable
    # Get events happening in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Player Position (Two arguments are passed, screen_width and screen_height)
    player.update_plyr_position(screen_width, screen_height)

    # Update Enemy
    enemy_group.update()

    # Draw background
    screen.blit(background, (0, 0))

    # Drawing player
    player.draw_plyr(screen)

    # Drawing enemies
    enemy_group.draw(screen)

    # Flip screen so user can see it
    pygame.display.flip()

    # Slow loop to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
