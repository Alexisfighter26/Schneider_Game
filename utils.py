import pygame
import random
import main

class Player:
    def __init__(self, screen):
        # Attributes of my player
        player = f'assets/sprites/sus.png'
        self.player_img = pygame.image.load(player).convert()
        self.player_rect = self.player_img.get_rect()

        self.player_x = random.randint(0,screen)
        self.player_x_dir = 1
        self.player_x_spd = screen()/(2*60)

# Motion variables
        self.num_update_positions_run = 0
        self.num_update_positions_run_2_change = random.randit(20,50)
