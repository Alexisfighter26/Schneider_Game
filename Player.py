import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image
        self.image = pygame.image.load('assets/sprites/sus.png').convert()
        self.rect = self.image.get_rect(center=(25, 422))  # Set the initial position of the player

        # Initialize the player's vertical velocity, jump power, gravity, and ground flag
        self.vel_y = 0
        self.jump_power = -14
        self.gravity = 0.6
        self.on_ground = False  # Flag to track whether the player is on the ground

    def update_plyr_position(self, screen_width, screen_height, platform_group):
        keys = pygame.key.get_pressed()  # Define keyboard mechanics

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Apply gravity and update vertical position
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Check collisions with platforms
        collisions = pygame.sprite.spritecollide(self, platform_group, False)
        for platform in collisions:
            if self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True  # Set the on_ground flag when landing on a platform
            elif self.vel_y < 0:
                self.rect.top = platform.rect.bottom
                self.vel_y = 0

        # Update the on_ground flag if the player is not colliding with any platforms
        if not collisions:
            self.on_ground = False

        # Apply screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0
            self.on_ground = True  # Set the on_ground flag when reaching the bottom

        # Jumping mechanism
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power

    def draw_plyr(self, screen):
        screen.blit(self.image, self.rect)  # Draw the player image onto the screen
