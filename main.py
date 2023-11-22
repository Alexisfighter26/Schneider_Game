import pygame
import random
import utils

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

bg = pygame.image.load(os.path.join('assets/sprites/sus.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

# (=====================Character Class======================)
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.position, 10)


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