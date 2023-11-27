import pygame
import random
'''import utils'''

# import time
# import sys


# Initialize Pygame
pygame.init()

# Create Pygame clock
clock = pygame.time.Clock()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning make_background.py.')
print('-------------------------------------------\n')

# Create the screen
screen = pygame.display.set_mode((1200, 486))

# Background
background = pygame.image.load("assets/sprites/Min_background.png")

print('Running game...')
running = True
while running:

    # store pygame events in a variable
    events = pygame.event.get()

    # Get events happening in window.
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    screen.blit(background, (0, 0))

    # Update screen based on your game.
    pygame.display.flip()
# (=================================================)

# Character intro
W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(('assets/sprites/sus.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

# (=====================Character Class======================)
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Attributes of player
        plyr = f'assets/sprites/sus.png'
        self.player_img = pygame.image.load(plyr).convert()
        self.player_rect = self.player_img.get_rect()

        self.player_x = random.randint(0, screen.get_width() - self.player_img.get_width())
        self.player_x_dir = 1
        self.player_x_spd = screen.get_width() / (2 * 60)

        self.y_bnd = screen.get_height()
        self.player_y = random.randint(0, self.y_bnd)
        self.player_y_dir = 1
        self.player_y_spd = self.y_bnd / (2 * 60)





# (=================================================)
john = Player(screen)
screen.blit(john)

# Show screen to user
run = True
while run:
    for event in pygame.event.get():  # Loop through a list of events
        if event.type == pygame.QUIT:  # See if the user clicks the red x
            run = False    # End the loop
            pygame.quit()  # Quit the game
            quit()