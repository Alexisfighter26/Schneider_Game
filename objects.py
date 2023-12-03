import pygame
import random

screen_width = 1200
screen_height = 428


class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/yellowGem.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.points = 10

    def set_random_position(self, screen_width, screen_height, platform_group):
        valid_position = False
        while not valid_position:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, screen_height - self.rect.height)

            collisions = pygame.sprite.spritecollide(self, platform_group, False)
            if not collisions:
                valid_position = True

class HealthItem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/greenCrystal.png').convert_alpha()
        self.rect = self.image.get_rect()

    def set_random_position(self, screen_width, screen_height, platform_group):
        valid_position = False
        while not valid_position:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, screen_height - self.rect.height)

            collisions = pygame.sprite.spritecollide(self, platform_group, False)
            if not collisions:
                valid_position = True

    def interact(self, player):
        # Some logic to handle interaction with the player
        player.increase_health(20)

'''class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/yellowGem.png').convert()
        self.rect = self.image.get_rect()
        self.points = 10

    def set_random_position(self, screen_width, screen_height, platform_group):
        valid_position = False
        while not valid_position:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, (screen_height - 64) - (self.rect.height - 128))

            collisions = pygame.sprite.spritecollide(self, platform_group, False)
            if not collisions:
                valid_position = True

    def set_random_position(self, screen_width, screen_height):
        # Set the position of the jewel randomly within the screen boundaries
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, (screen_height) - (self.rect.height)

class HealthItem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/greenCrystal.png').convert()
        self.rect = self.image.get_rect()

    def set_random_position(self, screen_width, screen_height, platform_group):
        valid_position = False
        while not valid_position:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, screen_height - self.rect.height)

            collisions = pygame.sprite.spritecollide(self, platform_group, False)
            if not collisions:
                valid_position = True

    def set_random_position(self, screen_width, screen_height):
        # Set the position of the health item randomly within the screen boundaries
        self.rect.x = random.randint(0, (screen_width - self.rect.width))
        self.rect.y = random.randint(0, (screen_height - self.rect.height))

    def interact(self, player):
        # Some logic to handle interaction with the player
        player.increase_health(20)'''


