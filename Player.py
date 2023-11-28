import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # The Player class inherits from pygame.sprite.Sprite
        self.image = pygame.image.load('assets/sprites/sus.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)  # Starting position
        self.image.set_colorkey((251, 251, 251))  # Set color key as a tuple

    def update_plyr_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    # This just draws the character onto the screen. (blit)
    def draw_plyr(self, screen):
        screen.blit(self.image, self.rect)
