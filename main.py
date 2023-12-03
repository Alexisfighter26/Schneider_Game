import sys
import pygame
from pygame import mixer
from Player import Player
from Enemies import Enemy
from Background import create_platforms
from loading_screens import *
from objects import Jewel
import math

# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Defining screen dimensions (easier to set bounds for character)
screen_width = 1200
screen_height = 486

# =========================================== Create the screen =========================================== #

screen = pygame.display.set_mode((screen_width, screen_height))

# ------------- Intro Screen ----------- #

intro_screen(screen)

# ----------------------Background-------------------- #

background = pygame.image.load("assets/sprites/set1_background.png").convert()
tiles = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
tiles2 = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
hills = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()
hills2 = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()

# ---------------------------- Creating the obstructions / platforms ------------------ #

platform_group = pygame.sprite.Group()
create_platforms(platform_group)

# -------------------- Background Sound --------------------------------#

mixer.init()
mixer.music.load("assets/sound/backgroundmusic.ogg")
mixer.music.play()

# ================ Creating  Entities ===================== #

# Instance of Player
player = Player()

# ------------- Jewel instance ----------------- #
# Create group instance of Jewel
jewel_group = pygame.sprite.Group()
# The instance of Jewel
jewel1 = Jewel()
# Creating an instance of Enemy and adding it to the enemy_group
jewel_group.add(jewel1)

# ------------- End of Jewel instance ----------------- #

# ------------- Enemies instance ----------------- #
# Create group instance of Enemy
enemy_group = pygame.sprite.Group()
# The instance of enemies
enemy1 = Enemy()
# Creating an instance of Enemy and adding it to the enemy_group
enemy_group.add(enemy1)
# ------------- Enemies instance done ----------------- #


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

    # ====== Drawing Entities ============= #

    # Drawing player
    player.draw_plyr(screen)

    # Drawing enemies
    enemy_group.draw(screen)

    # Drawing Jewels
    jewel_group.draw(screen)

    #------- Updating the Points ---------#
    player.draw_points(screen)
    player.draw_health(screen)

    # ====== Entities Update ============================================= #

    # Update Player Position (Two arguments are passed, screen_width and screen_height)
    player.update_plyr_position(screen_width, screen_height, platform_group)

    # Update Enemy
    #enemy_group.update()
    for enemy in enemy_group:
        enemy.update(player)
 
    # =================== Interactions between Jewels and player ============================ #

    jewels_collected = pygame.sprite.spritecollide(player, jewel_group, True)
    for jewel in jewels_collected:
        player.points += jewel.points  # Increase player's points upon collision with a jewel

        # Create a new instance of the jewel and add it to the jewel group
        new_jewel = Jewel()
        jewel_group.add(new_jewel)

    # =================== Interactions between enemy and player ============================ #

    # Inside your game loop handling collisions between the player and enemy
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in enemy_hit_list:
        # Subtract health when player collides with an enemy
        player.health -= 10  # Reduce player's health by 10 (adjusting this value)


        # For example, if enemy has a knockback effect:
        enemy.rect.x += 20  # Move the enemy back upon collision

    # Check if player's health reaches zero
    if player.health <= 0:
        game_over_screen(screen)  # Display the game over screen
        running = False  # Exit the game loop

    # ====================================== DONE =============================================== #

    # Flip screen so user can see it
    pygame.display.flip()

    # Slow loop to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
