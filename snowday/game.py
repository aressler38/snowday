"""
This is the game class
"""
import sys
import pygame
from snowday.bgm import Bgm

DISPLAYSURF = pygame.display.set_mode((400, 300))


FramePerSec = pygame.time.Clock()

class Game:
    HEIGHT = 450
    WIDTH = 400
    ACC = 0.5
    FRIC = -0.12
    FPS = 60

    def __init__(self, **kwargs):
        """ Setup stuff in here """
        pygame.init()
        caption = kwargs.get('caption', 'Game')
        pygame.display.set_caption(caption)
        self.displaysurface = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.bgm = Bgm()

    def bgm_on(self):
        """ Play the background music """
        self.bgm.play()




    def run(self):
        """ Run the game loop """
        self.bgm_on()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()
                    sys.exit()

            self.displaysurface.fill((0,0,0))

            #for entity in all_sprites:
            #    self.displaysurface.blit(entity.surf, entity.rect)

            pygame.display.update()
            FramePerSec.tick(Game.FPS)

