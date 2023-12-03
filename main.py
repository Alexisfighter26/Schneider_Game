import sys
import pygame
from pygame import mixer
from Player import Player
from Enemies import Enemy
from Background import Platform
import math


# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()
FPS = 100

# Defining screen dimensions (easier to set bounds for character)
screen_width = 1200
screen_height = 486

# =========================================== Create the screen =========================================== #

screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load("assets/sprites/scrolling.jpg").convert()
background_width = background.get_width()
background_rect = background.get_rect()

# ========================= Creating the obstructions / platforms ================== #

platform_group = pygame.sprite.Group()

# Create Instance of Platforms
platform1 = Platform(1136, 64)
platform2 = Platform(0, 422)
platform3 = Platform(64, 422)
platform4 = Platform(128, 422)
platform5 = Platform(192, 422)
platform6 = Platform(256, 422)
platform7 = Platform(320, 200)


# Add platforms to the platform group

platform_group.add(platform1, platform2, platform3,platform4, platform5, platform6, platform7)

# define scrolling variable (will prob delete)
scroll = 0
tiles = math.ceil(screen_width / background_width) + 1

# Background Sound!
mixer.init()
mixer.music.load("assets/sound/backgroundmusic.ogg")
mixer.music.play()

# ================ Creating  Entities ===================== #

# Instance of Player
player = Player()

# Create group Instance of Enemy
enemy_group = pygame.sprite.Group()

# The instance of enemies
enemy1 = Enemy()

# Creating an instance of Enemy and adding it to the enemy_group
enemy_group.add(enemy1)

# ===== END OF CREATION ====== #

# Main Game loop
print('Running game...')
running = True
while running:
    # store pygame events in a variable
    # Get events happening in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === Scrolling Screen =============================================== #

        clock.tick(FPS)

        # draw scrolling background
        for i in range(0, tiles):
            screen.blit(background, (i * background_width + scroll, 0))
            background_rect.x = i * background_width + scroll
            pygame.draw.rect(screen, (255, 0, 0), background_rect, 1)

        # scroll background
        scroll -= 30

        # reset scroll
        if abs(scroll) > background_width:
            scroll = 0

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # ====== Draw Background ============= #

    # Draw background (scrolling)
    for i in range(tiles):
        screen.blit(background, (i * background_width + scroll, 0))

    # Draw Platforms
    platform_group.draw(screen)

    # ====== Draw Entities ============= #

    # Drawing player
    player.draw_plyr(screen)

    # Drawing enemies
    enemy_group.draw(screen)

    # ====== Entities Update ============================================= #

    # Update Player Position (Two arguments are passed, screen_width and screen_height)
    player.update_plyr_position(screen_width, screen_height, platform_group)

    # Update Enemy
    enemy_group.update()

    # ====== DONE ============= #
    # Flip screen so user can see it
    pygame.display.flip()

    # Slow loop to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
