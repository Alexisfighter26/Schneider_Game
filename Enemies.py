import pygame
import random

# It kept saying screen_width is not defined so I just redefined it.
screen_width = 1200
screen_height = 428

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/bat_fly.png').convert_alpha()
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

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0
            self.on_ground = True  # Set on_ground flag when reaching the bottom
