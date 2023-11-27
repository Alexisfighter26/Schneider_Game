import pygame


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

    #Player.draw(screen)

    # Draw background.
    screen.blit(background, (0, 0))

    # Update screen based on your game.
    pygame.display.flip()