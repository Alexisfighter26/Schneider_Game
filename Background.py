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

def create_platforms(platform_group):
    # Create Instance of Platforms
    platform1 = Platform(1136, 64)
    platform2 = Platform(0, 422)
    platform3 = Platform(64, 422)
    platform4 = Platform(128, 422)
    platform5 = Platform(192, 422)
    platform6 = Platform(256, 422)
    platform7 = Platform(320, 422)
    platform8 = Platform(384, 422)
    platform9 = Platform(448, 422)
    platform10 = Platform(512, 422)
    platform11 = Platform(576, 422)

        # Add platforms to the platform group
    platform_group.add(platform1, platform2, platform3, platform4,
                        platform5, platform6, platform7, platform8, platform9,
                        platform10, platform11)

'''import pygame
from Background import Platform

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

    def create_platforms(platform_group):
        # Create Instance of Platforms
        platform1 = Platform(1136, 64)
        platform2 = Platform(0, 422)
        platform3 = Platform(64, 422)
        platform4 = Platform(128, 422)
        platform5 = Platform(192, 422)
        platform6 = Platform(256, 422)
        platform7 = Platform(320, 422)
        platform8 = Platform(384, 422)
        platform9 = Platform(448, 422)
        platform10 = Platform(512, 422)
        platform11 = Platform(576, 422)

        # Add platforms to the platform group

        platform_group.add(platform1, platform2, platform3, platform4,
                           platform5, platform6, platform7, platform8, platform9
                           , platform10, platform11)'''