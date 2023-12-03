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
        text = font.render("Treasure hunter", True, (255, 255, 255))  # Text, antialiasing, color
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        # Additional instructions or information
        instructions = font.render("Objective: Collect as MANY yellow Gems as possible", True, (255, 255, 255))
        instructions_rect = instructions.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        screen.blit(instructions, instructions_rect)

        # Additional instructions or information
        instructions2 = font.render("Press SPACE to start, arrow keys and space bar for movement", True, (255, 255, 255))
        instructions2_rect = instructions2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(instructions2, instructions2_rect)

        instructions3 = font.render(" TIPS : Green crystals for health, BEWARE! lots of gems = lots of enemies ", True,
                                    (255, 255, 255))
        instructions3_rect = instructions2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))
        screen.blit(instructions3, instructions3_rect)

        pygame.display.update()

 # ================================== GAME OVER SCREEN ====================================== #
def game_over_screen(screen):
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, (255, 0, 0))  # Red text
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Black background
        screen.blit(game_over_text, text_rect)

        pygame.display.update()