"""
This is the game class
"""
import sys
import math
import pygame
from pygame.math import Vector2
import pygame.sprite
import pygame.mouse
from snowday.bgm import Bgm
from snowday.sprites.snowflake import Snowflake
from snowday.sprites.potato_gun import PotatoGun

DISPLAYSURF = pygame.display.set_mode((400, 300))



class Game:
    HEIGHT = 600
    WIDTH = 800
    ACC = 0.5
    FRIC = -0.12
    FPS = 22

    def __init__(self, **kwargs):
        """ Setup stuff in here """
        pygame.init()
        caption = kwargs.get('caption', 'Game')
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.displaysurface = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.bgm = Bgm()

    def get_gun_angle(self):
        """
        Calculate the angle the potato gun should point based on the mouse cursor.
        """
        vec2 = pygame.mouse.get_pos()
        y = Game.HEIGHT - vec2[1]
        x =  vec2[0] - Game.WIDTH / 2
        angle = int(math.atan2(y, x) * 180 / math.pi) - 90
        return angle

    def run(self):
        """ Run the game loop """
        self.bgm.play()

        snowflakes = pygame.sprite.Group()

        platform = pygame.sprite.Sprite()
        platform.rect = pygame.Rect(0, 40, Game.WIDTH, 50)
        platform.rect.bottom = Game.HEIGHT
        platform.rect.width = Game.WIDTH
        platform.image = pygame.Surface([platform.rect.width, platform.rect.height])
        platform.image.fill((255, 255, 255))

        snowflake = Snowflake()
        snowflakes.add(snowflake)

        potato_gun = PotatoGun(Vector2(Game.WIDTH / 2, Game.HEIGHT))

        # Keep track of when the player finishes clicking a mouse button.
        click_start = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()
                    sys.exit()

            # Draw a black background.
            self.displaysurface.fill((0, 0, 0))
            # Draw the ground.
            self.displaysurface.blit(platform.image, platform.rect)

            # Update the snowflakes sprite group causing them to fall.
            snowflakes.update()
            # Check if the snowflake hit the ground.
            for snowflake in pygame.sprite.spritecollide(platform, snowflakes, True):
                print('melt')
                snowflake = Snowflake()
                snowflakes.add(snowflake)
            # Draw the snowflakes that didn't hit the ground.
            snowflakes.draw(self.displaysurface)

            # Calculate the potato gun angle based on the mouse cursor.
            angle = self.get_gun_angle()
            # Aim the gun.
            potato_gun.rotate(angle)
            # Draw the potato gun
            self.displaysurface.blit(potato_gun.image, potato_gun.rect)

            # See if the player finished clicking a shoot button.
            for mouse_btn in pygame.mouse.get_pressed(3):
                if mouse_btn:
                    click_start = True
                    break
                if click_start:
                    potato_gun.shoot_potato()
                    click_start = False

            # Update the display and clock.
            pygame.display.update()
            self.clock.tick(Game.FPS)


