import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__() # Super init initializes the sprite

        # Attributes of player
        self.image = pygame.image.load('assets/sprites/sus.png').convert()
        self.image.set_colorkey((251,251,251)) # Making this a tuple

        # This makes the player move at 240 px/seconds cause (px/loop)
        self.plyr_spd = 4

        # Initial position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Update player position
        def update_plyr_pos(self):
            self.x += self.plyr_spd
            self.y += self.plyr_spd

        # Creating my player object
        player = Player(x=50, y=100)