import pygame

platform_width = 64
platform_height = 64
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((platform_width, platform_height))
        self.image = pygame.image.load('assets/sprites/tileBrown_02.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y