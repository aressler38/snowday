"""
This is the game class
"""

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

