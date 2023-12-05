import pygame
import random

# It kept saying screen_width is not defined so, I just redefined it.
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
        if player.rect.centerx > self.rect.centerx:  # If player is to the right of the enemy
            self.rect.x += self.speed  # Move enemy right
        elif player.rect.centerx < self.rect.centerx:  # If player is to the left of the enemy
            self.rect.x -= self.speed  # Move enemy left

        # Move the enemy towards the player along the y-axis
        if player.rect.centery > self.rect.centery:  # If player is below the enemy
            self.rect.y += self.speed  # Move enemy down
        elif player.rect.centery < self.rect.centery:  # If player is above the enemy
            self.rect.y -= self.speed  # Move enemy up

        # Boundary checking to ensure the enemy stays within the screen limits
        if self.rect.left < 0:  # If the enemy exceeds the left boundary
            self.rect.left = 0  # Set the enemy's left side to the screen's left edge
        elif self.rect.right > screen_width:  # If the enemy exceeds the right boundary
            self.rect.right = screen_width  # Set the enemy's right side to the screen's right edge

        if self.rect.top < 0:  # If the enemy exceeds the top boundary
            self.rect.top = 0  # Set the enemy's top side to the screen's top edge
        elif self.rect.bottom > screen_height:  # If the enemy exceeds the bottom boundary
            self.rect.bottom = screen_height  # Set the enemy's bottom side to the screen's bottom edge
            self.vel_y = 0  # Stop vertical movement
            self.on_ground = True  # Set on_ground when reaching the bottom

