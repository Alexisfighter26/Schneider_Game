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

# Create Pygame clock (controls how fast the game runs)
clock = pygame.time.Clock()

# Defining screen dimensions (e5asier to set bounds for character)

screen_width = 1200
screen_height = 486

# =========================================== Create the screen =========================================== #

screen = pygame.display.set_mode((screen_width, screen_height))

# ------------- Intro Screen ----------- #

# This is a function that passes 'screen' through the function
intro_screen(screen)

# ----------------------Background-------------------- #

background = pygame.image.load("assets/sprites/set1_background.png").convert()
tiles = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
tiles2 = pygame.image.load("assets/sprites/set1_tiles.png").convert_alpha()
hills = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()
hills2 = pygame.image.load("assets/sprites/set1_hills.png").convert_alpha()

# -------------------- Creating the obstructions / platforms ------------------ #

# initializes an empty sprite group that will hold instances of my platform sprite
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

# Create group instance of Jewel (same thing as Platform) # initializes an empty sprite group
# that will hold instances of my platform sprite
jewel_group = pygame.sprite.Group()
HealthItem_group = pygame.sprite.Group()

# The instance of Jewel. It sets a random position after a jewel s hit
jewel1 = Jewel()
# platform ensures It doesn't spawn in the platforms (checks collisions)
jewel1.set_random_position(screen_width, screen_height, platform_group)
# Adds the jewel1 instance to a group called jewel_group
jewel_group.add(jewel1)


# Instance of Health Item ( same thing as Jewel )
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


# ================================= MAIN GAME LOOP ================================= #
print('Running game...')
running = True
while running:
    # store pygame events in a variable
    # Get events happening in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # Runs the loop for 60 frames per second

    # ====== Draw Background ============= #
    screen.blit(background, (0, 0))
    screen.blit(tiles, (0, 0))
    screen.blit(tiles2, (640, 0))
    screen.blit(hills, (0, 0))
    screen.blit(hills2, (640, 0))

    # ---------------- Draw Platforms- --------------- #
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

    # Update Enemy (Passing the player object as an argument allows enemy to utilize the information stored in player object. )
    for enemy in enemy_group:
        enemy.update(player)

    # =================== Interactions between Jewels and player ============================ #

    jewels_collected = pygame.sprite.spritecollide(player, jewel_group, True)
    # for loop in which checks each collided jewel with player
    for jewel in jewels_collected:
        player.points += jewel.points  # Increase player's points upon collision with a jewel

        # Create a new instance of the jewel and add it to the jewel group
        new_jewel = Jewel()
        jewel_group.add(new_jewel)
        new_jewel.set_random_position(screen_width, screen_height, platform_group)
        # show the points onto the screen
        player.draw_points(screen)
    # =================== Interactions between objects/Enemy and player ============================ #

    #--------- Health objects ----------- #
    collided_health_items = pygame.sprite.spritecollide(player, HealthItem_group, True) # Detecting collisions between player and health object
    for health_item in collided_health_items: # For each health item the player collides with
        health_item.interact(player) # interact between the health item and the player

        new_health_item = HealthItem() # Create a new health item
        new_health_item.set_random_position(screen_width, screen_height, platform_group)  # New health item randomly on the screen
        HealthItem_group.add(new_health_item)  # Add the new health item to the group of health items

# ---- Drawing on screen --- #
    jewel_group.draw(screen)
    HealthItem_group.draw(screen)

# -------------- Enemy / player interaction ---------------- #

    # Inside your game loop handling collisions between the player and enemy
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in enemy_hit_list:
        # Subtract health when player collides with an enemy
        player.health -= 5  # Reduce player's health by 5 (adjusting this value)

        #Enemy has a knockback effect:
        enemy.rect.x += 30  # Move the enemy back upon

       # Condition to spawn an enemy every 10 points
        if player.points % 10 == 0 and spawn_enemy:  # Spawning an enemy every 20 points

            #can_spawn_enemy = True
            new_enemy = Enemy()  # Create a new enemy instance
            # Set the initial position of the new enemy to random coordinates
            new_enemy.rect.x = random.randint(0, screen_width - new_enemy.rect.width)
            new_enemy.rect.y = random.randint(0, screen_height - new_enemy.rect.height)

            new_enemy = Enemy()
            # Add the new enemy to the enemy group
            enemy_group.add(new_enemy)
            # Set the flag to False to prevent spawning multiple enemies at once
            can_spawn_enemy = False
            spawn_enemy = True

    # Check if player's health reaches zero or less
    if player.health <= 0:
        game_over_screen(screen, player)  # Display the game over screen
        running = False  # Exit the game loop

        # Flip screen so user can see it
        pygame.display.flip()

        # ====================================== DONE =============================================== #

    # Flip screen so user can see it
    pygame.display.flip()



# Quit pygame
pygame.quit()
sys.exit()


