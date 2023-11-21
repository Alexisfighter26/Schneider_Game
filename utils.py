import pygame
import time

class player:
    def __init__(self):
        player = f'assets/sprites/sus.png'
        self.player_img = pygame.image.load(player).convert()