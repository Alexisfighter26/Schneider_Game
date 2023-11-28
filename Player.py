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
        self.jump_power = -10  # Initial force applied when jumping
        self.gravity = 0.6  # Gravity to bring the player back down
        self.max_speed = 5  # Maximum horizontal movement speed

    # This function updates my player position
    def update_plyr_position(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Apply horizontal velocity (adds the x position with the x velocity "positioning")
        self.rect.x += self.vel_x

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

    # Drawing player on screen
    def draw_plyr(self, screen):
        screen.blit(self.image, self.rect)
