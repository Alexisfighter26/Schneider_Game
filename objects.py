import pygame
import random

screen_width = 1200
screen_height = 428
class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Same thing as player, initialize image, position and physics
        self.image = pygame.image.load('assets/sprites/yellowGem.png').convert_alpha()
        # creates an object around my character (easily able to manipulate collisions, and positioning)
        self.rect = self.image.get_rect()
        self.set_random_position(screen_width, screen_height)
        self.points = 10

    def set_random_position(self, screen_width, screen_height):
        # Set the position of the jewel randomly within the screen boundaries
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)



