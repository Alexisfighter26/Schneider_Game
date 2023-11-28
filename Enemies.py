import pygame
import random

# It kept saying screen_width is not defined so I just redefined it.
screen_width = 1200
screen_height = 428
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Same thing as player, initialize image, position and physics
        self.image = pygame.image.load('assets/sprites/alienBlue.png').convert()
        # creates an object around my character (easily able to manipulate collisions, and positioning)
        self.rect = self.image.get_rect()
        # Where is he spawning
        self.rect.center = (100,100)
        self.health = 50
        self.speed = 4
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Set initial position to a random location within the screen boundaries
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)

    def update(self):
        self.rect.x += self.speed

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed = -self.speed
