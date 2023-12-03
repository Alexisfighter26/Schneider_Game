import pygame
import random

# It kept saying screen_width is not defined so I just redefined it.
screen_width = 1200
screen_height = 428

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/alienBlue.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 2  # Adjust this value to control the enemy's speed

    def update(self, player):
        # Move the enemy towards the player along the x-axis
        if player.rect.centerx > self.rect.centerx:
            self.rect.x += self.speed
        elif player.rect.centerx < self.rect.centerx:
            self.rect.x -= self.speed

        # Move the enemy towards the player along the y-axis
        if player.rect.centery > self.rect.centery:
            self.rect.y += self.speed
        elif player.rect.centery < self.rect.centery:
            self.rect.y -= self.speed
