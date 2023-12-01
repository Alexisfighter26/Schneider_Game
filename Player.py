import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # The Player class inherits from pygame.sprite.Sprite

        self.image = pygame.image.load('assets/sprites/sus.png').convert()
        # creates an object around my character (easily able to manipulate collisions, and positioning)
        self.rect = self.image.get_rect()

        self.rect.center = (25, 600)
        # Starting position
        # (The values are based on specific image size and screen dimension)

        self.image.set_colorkey((251, 251, 251))  # Set color key as a tuple
        self.vel_x = 0  # Horizontal velocity
        self.vel_y = 0  # Vertical velocity
        self.jump_power = -15  # Force applied when jumping
        self.gravity = 0.6  # Gravity to bring the player back down
        self.max_speed = 10  # Maximum horizontal movement speed (bc im only moving in x dir)

    # This function updates my player position
    def update_plyr_position(self, screen_width, screen_height, platform_group):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Prevent the player from going off the screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        # Jumping mechanism
        if keys[pygame.K_SPACE] and self.rect.bottom >= screen_height:
            self.vel_y = self.jump_power

        # Apply gravity
        self.vel_y += self.gravity

        # Update vertical position
        self.rect.y += self.vel_y

        # Prevent the player from going off the screen vertically
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0

        # Check for collision with platforms
        collisions = pygame.sprite.spritecollide(self, platform_group, False)
        for platform in collisions:
            if self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
            elif self.vel_y < 0:
                self.rect.top = platform.rect.bottom
                self.vel_y = 0

            # Jumping mechanism (can jump anytime the player is in contact with a platform)
            if keys[pygame.K_SPACE] and (collisions or self.rect.bottom >= screen_height):
                self.vel_y = self.jump_power

            # Prevent the player from going off the screen vertically
            if self.rect.bottom >= screen_height:
                self.rect.bottom = screen_height
                self.vel_y = 0


    # Drawing player on screen
    def draw_plyr(self, screen):
        screen.blit(self.image, self.rect)
