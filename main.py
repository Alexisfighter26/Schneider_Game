import sys
import pygame
from pygame import mixer
from Player import Player
from Enemies import Enemy
from Background import create_platforms
from loading_screens import *
from objects import *

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

# -------------------- Creating the obstructions / platforms ------------------ #

platform_group = pygame.sprite.Group()
create_platforms(platform_group)

# -------------------- Background Sound --------------------------------#

mixer.init()
mixer.music.load("assets/sound/backgroundmusic.ogg")
mixer.music.play()

# ================ Creating  Entities ===================== #

# Instance of Player (so attributes are accessible)
player = Player()

# ------------- Jewel/HealthItem instance ----------------- #

# Create group instance of Jewel
jewel_group = pygame.sprite.Group()
HealthItem_group = pygame.sprite.Group()

# The instance of Jewel
jewel1 = Jewel()
jewel1.set_random_position(screen_width, screen_height, platform_group)
jewel_group.add(jewel1)

# Instance of Health Item
healthItem1 = HealthItem()
healthItem1.set_random_position(screen_width, screen_height, platform_group)
HealthItem_group.add(healthItem1)

# ------------- Enemies instance ----------------- #
# Create group instance of Enemy
enemy_group = pygame.sprite.Group()
# The instance of enemies
enemy1 = Enemy()
# Creating an instance of Enemy and adding it to the enemy_group
enemy_group.add(enemy1)
# ------------- Enemies instance done ----------------- #
spawn_enemy = True

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
    screen.blit(hills, (0, 0))
    screen.blit(hills2, (640, 0))

    # Draw Platforms
    platform_group.draw(screen)

    # ====== Drawing Entities ============= #

    # Drawing player
    player.draw_plyr(screen)

    # Drawing enemies
    enemy_group.draw(screen)
    # ------- Updating the Points ---------#

    player.draw_points(screen)
    player.draw_health(screen)

    # ====== Entities Update ============================================= #

    # Update Player Position (Two arguments are passed, screen_width and screen_height)
    player.update_plyr_position(screen_width, screen_height, platform_group)

    # Update Enemy
    for enemy in enemy_group:
        enemy.update(player)

    # =================== Interactions between Jewels and player ============================ #

    jewels_collected = pygame.sprite.spritecollide(player, jewel_group, True)
    for jewel in jewels_collected:
        player.points += jewel.points  # Increase player's points upon collision with a jewel

        # Create a new instance of the jewel and add it to the jewel group
        new_jewel = Jewel()
        jewel_group.add(new_jewel)
        new_jewel.set_random_position(screen_width, screen_height, platform_group)


        player.draw_points(screen)
    # =================== Interactions between objects/Enemy and player ============================ #

    #--------- Health objects ----------- #


    collided_health_items = pygame.sprite.spritecollide(player, HealthItem_group, True)
    for health_item in collided_health_items:
        health_item.interact(player)

        new_health_item = HealthItem()
        new_health_item.set_random_position(screen_width, screen_height, platform_group)
        HealthItem_group.add(new_health_item)

# ---- Drawing on screen --- #
    jewel_group.draw(screen)
    HealthItem_group.draw(screen)

# -------------- Enemy / player interaction ---------------- #

    # Inside your game loop handling collisions between the player and enemy
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in enemy_hit_list:
        # Subtract health when player collides with an enemy
        player.health -= 5  # Reduce player's health by 5 (adjusting this value)

        # #nemy has a knockback effect:
        enemy.rect.x += 30  # Move the enemy back upon collision

        # Condition to spawn an enemy based on points
        if player.points >= 20 and spawn_enemy:
            new_enemy = Enemy()  # Create a new enemy instance

            # Set the initial position of the new enemy to random coordinates
            new_enemy.rect.x = random.randint(0, screen_width - new_enemy.rect.width)
            new_enemy.rect.y = random.randint(0, screen_height - new_enemy.rect.height)

            # Add the new enemy to the enemy group
            enemy_group.add(new_enemy)

            # Set the flag to False to prevent spawning multiple enemies at once
            spawn_enemy = False

    # Check if player's health reaches zero or less
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
