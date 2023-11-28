import pygame
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/platforms/tileBlue_05.png').convert()
        self.rect = self.image.get_rect(topleft=(x, y))
