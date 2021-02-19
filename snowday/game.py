"""
This is the game class
"""
import sys
import math
import pygame
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

    def bgm_on(self):
        """ Play the background music """
        self.bgm.play()

    def get_gun_angle(self):
        vec2 = pygame.mouse.get_pos()
        y = Game.HEIGHT - vec2[1]
        x =  vec2[0] - Game.WIDTH / 2

        angle = int(math.atan2(y, x) * 180 / math.pi) - 90
        print(angle)
        return angle


    def run(self):
        """ Run the game loop """
        self.bgm_on()

        snowflakes = pygame.sprite.Group()

        platform = pygame.sprite.Sprite()
        platform.rect = pygame.Rect(0, 40, Game.WIDTH, 50)
        platform.rect.bottom = Game.HEIGHT
        platform.rect.width = Game.WIDTH
        platform.image = pygame.Surface([platform.rect.width, platform.rect.height])
        platform.image.fill((255, 255, 255))

        snowflake = Snowflake()
        snowflakes.add(snowflake)

        potato_gun = PotatoGun()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()
                    sys.exit()

            self.displaysurface.fill((0, 0, 0))

            snowflakes.update()
            snowflakes.draw(self.displaysurface)

            #for sprite in snowflakes:
            #    self.displaysurface.blit(sprite.image, sprite.rect)

            for snowflake in pygame.sprite.spritecollide(platform, snowflakes, True):
                print('melt')
                snowflake = Snowflake()
                snowflakes.add(snowflake)


            self.displaysurface.blit(platform.image, platform.rect)

            angle = self.get_gun_angle()
            potato_gun.rotate(angle)
            potato_gun.rect.center = (Game.WIDTH / 2, Game.HEIGHT)
            potato_gun.rect.y -= potato_gun.rect.height / 2
            self.displaysurface.blit(potato_gun.image, potato_gun.rect)

            pygame.display.update()
            self.clock.tick(Game.FPS)


