import pygame
import sys

def intro_screen(screen):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game on spacebar press
                    intro = False

        # Fill the screen with a background color
        screen.fill((0, 0, 0))  # Black background

        # Render and display text on the screen
        font = pygame.font.Font(None, 36)
        text = font.render("Your Game Title", True, (255, 255, 255))  # Text, antialiasing, color
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        # Additional instructions or information
        instructions = font.render("Press SPACE to start", True, (255, 255, 255))
        instructions_rect = instructions.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        screen.blit(instructions, instructions_rect)

        pygame.display.update()
