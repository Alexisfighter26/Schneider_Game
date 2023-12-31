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
                if event.key == pygame.K_SPACE:  # Start the game on space bar
                    intro = False

        # Fill the screen with a background color
        screen.fill((32, 86, 140))  # Black background

        # Render and display text on the screen
        font = pygame.font.Font('assets/font/Black_Crayon.ttf', 36)
        text = font.render("Treasure hunter", True, (0, 0, 0))  # Text, antialiasing, color

        # Adjust vertical position to move the text higher on the screen
        vertical_offset = 100  # Change this value to move the text higher or lower
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - vertical_offset))
        screen.blit(text, text_rect)

        # Render and display directions with a smaller font size
        directions_font = pygame.font.Font(None, 36)  # Smaller font size for the directions

        # Adjust vertical position to move the text higher on the screen
        vertical_offset = 100  # Change this value to move the text higher or lower
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - vertical_offset))
        screen.blit(text, text_rect)

        # Additional instructions or information
        instructions = font.render("Objective: Collect as MANY yellow Gems as possible", True, (255, 255, 255))
        instructions_rect = instructions.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        screen.blit(instructions, instructions_rect)

        # Additional instructions or information
        instructions2 = font.render("Press SPACE to start, arrow keys and space bar for movement", True, (255, 255, 255))
        instructions2_rect = instructions2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(instructions2, instructions2_rect)

        instructions3 = font.render(" TIPS : Green crystals for health, BEWARE! Avoid the Bats! ", True,
                                    (255, 255, 255))
        instructions3_rect = instructions3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))
        screen.blit(instructions3, instructions3_rect)


        pygame.display.update()

 # ================================== GAME OVER SCREEN ====================================== #

def game_over_screen(screen, player):
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over, You Died!", True, (255, 0, 0))  # Red text
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Display player's final score or relevant game-over information
    score_text = font.render(f"You collected: {player.points} pounds of treasure", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

# ------ Background Backdrop ------- #

    # Fill screen with a black background
    screen.fill((0, 0, 0))

    # Showing the text from functions onto the screen
    screen.blit(game_over_text, text_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()
    pygame.time.delay(3000) # Keeps the background screen to continue running

