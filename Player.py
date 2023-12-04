import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image
        self.image = pygame.image.load('assets/sprites/alienGreen_walk.png').convert_alpha()
        self.rect = self.image.get_rect(center=(25, 422))  # Set the initial position of the player

        # Initialize the player's vertical velocity, jump power, gravity, and ground flag
        self.vel_y = 0
        self.jump_power = -16
        self.gravity = 0.6
        self.on_ground = False  # Tracks whether the player is on the ground
        self.health = 100
        self.max_health = 300
        self.points = 0

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
                self.on_ground = True  # Set on_ground when landing on a platform
            elif self.vel_y < 0:
                self.rect.top = platform.rect.bottom
                self.vel_y = 0

        # Update the on_ground if the player is not colliding with any platforms
        if not collisions:
            self.on_ground = False

        # Apply screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0
            self.on_ground = True  # Set on_ground flag when reaching the bottom

        # Jumping mechanism
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power

    def draw_health(self, screen):
        font = pygame.font.Font(None, 36)
        health_text = font.render(f'Health: {self.health}', True, (255, 255, 255))
        text_position = (10, screen.get_height() - health_text.get_height() - 10)  # Bottom left position
        screen.blit(health_text, text_position)

    def draw_points(self, screen):
        font = pygame.font.Font(None, 36)
        points_text = font.render(f'Points: {self.points}', True, (255, 255, 255))
        text_position = (10, 10)  # Top-left corner
        screen.blit(points_text, text_position)

    def increase_health(self, amount):
        # Check if the current health is less than the maximum health
        if self.health < self.max_health:
            self.health += amount  # Increase player's health by the specified amount

            # Check if the health exceeds the maximum limit
            if self.health > self.max_health:
                self.health = self.max_health  # Cap the health to the maximum limit

    def draw_plyr(self, screen):
        screen.blit(self.image, self.rect)  # Draw the player image onto the screen
