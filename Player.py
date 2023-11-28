import pygame

class Player:
    def __init__(self, x=0, y=0):

        # Attributes of player
        self.image = pygame.image.load('assets/sprites/sus.png').convert()
        self.image.set_colorkey(251,251,251)

        # This makes the player move at 240 px/seconds cause (px/loop)
        self.plyr_spd = 4


        # Update player position
        def update_plyr_pos(self):
            self.x += self.plyr_spd
            self.y += self.plyr_spd
