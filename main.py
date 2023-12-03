import sys
import pygame
from pygame import mixer
from Player import Player
from Enemies import Enemy
import math
from Background import create_platforms



# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Defining screen dimensions (easier to set bounds for character)
screen_width = 1200
screen_height = 486

# =========================================== Create the screen =========================================== #

# ================================TESTING ================ #
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load("assets/sprites/set1_background.png").convert()
tiles = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
tiles2 = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
hills = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()
hills2 = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()

#hills =
background_width = background.get_width()
background_rect = background.get_rect()

# ========================= Creating the obstructions / platforms ================== #

platform_group = pygame.sprite.Group()
create_platforms(platform_group)

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

    # ====== Draw Background ============= #
    screen.blit(background, (0, 0))
    screen.blit(tiles, (0, 0))
    screen.blit(tiles2, (640, 0))
    screen.blit(hills, (335, 0))
    screen.blit(hills2, (28, 0))

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

    # =================== Interactions between enemy and player ============================ #
    # Inside your game loop where you handle collisions between the player and enemy
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in enemy_hit_list:
        # Subtract health when player collides with an enemy
        player.health -= 10  # Reduce player's health by 10 (you can adjust this value)

        # You can add more logic here, such as enemy bounce-back or removing the enemy
        # For example, if enemy has a knockback effect:
        enemy.rect.x += 20  # Move the enemy back upon collision
    # ========================= DONE ========================= #

    # Flip screen so user can see it
    pygame.display.flip()

    # Slow loop to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
