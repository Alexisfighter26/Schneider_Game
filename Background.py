import pygame

platform_width = 64
platform_height = 64
screen_height = 486
screen_width = 1264

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((platform_width, platform_height))
        self.image = pygame.image.load('assets/sprites/tileBrown_02.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_platforms(platform_group):

    # Calculate the number of platforms needed to fill the bottom of the screen tells us that our screen width 1800,
    # divided by image pixel 64 is approx 18.75
    num_platforms = screen_width // platform_width

    # This loops num_platforms as defined above , it calculates the x coordinate, and sets the y coordinate to the bottom of the screen
    for i in range(num_platforms):
        platform = Platform(i * platform_width, screen_height - platform_height)
        platform_group.add(platform)


    # Specially placed platforms

    # Create Instance of Platforms
    platform1 = Platform(1136, 64)
    platform2 = Platform(600, 278)
    platform3 = Platform(664, 278)
    platform4 = Platform(536, 278)
    platform5 = Platform(192, 522)
    platform6 = Platform(256, 522)
    platform7 = Platform(320, 522)
    platform8 = Platform(384, 522)
    platform9 = Platform(448, 522)
    platform10 = Platform(512, 522)
    platform11 = Platform(576, 522)
    platform12 = Platform(640, 522)
    platform13 = Platform(704, 522)
    platform14 = Platform(768, 522)
    platform15 = Platform(832, 522)
    platform16 = Platform(896, 522)
    platform17 = Platform(500,500)
    platform18 = Platform(832, 522)
    platform19 = Platform(704, 422)
    platform20 = Platform(768, 422)
    platform21 = Platform(832, 422)

        # Add platforms to the platform group
    platform_group.add(platform1, platform2, platform3, platform4,
                        platform5, platform6, platform7, platform8, platform9,
                        platform10, platform11, platform12, platform13, platform14, platform15)