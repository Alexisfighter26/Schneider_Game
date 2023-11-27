import pygame
from utils import *

class Player:
    def __init__(self, x, y):
        # Attributes of player

        self.image = pygame.image.load('assets/sprites/sus.png').convert()

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center(x,y)


        # Setting Speed
        self.player_x_spd = plyr_spd
        self.player_y_spd = plyr_spd

        plyr_spd = 4



        # Drawing character
    def draw(self, screen):
        screen.blit(self.image, self.rect)