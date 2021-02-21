import math
import pkg_resources

import pygame
from pygame.math import Vector2
import pygame.sprite
import pygame.image
import pygame.transform
import pygame.time


class Crosshair(pygame.sprite.Sprite):

    IMAGE_PATH = pkg_resources.resource_filename(
        "snowday", "assets/sprites/crosshair.png"
    )

    CROSSHAIR = pygame.transform.scale(pygame.image.load(IMAGE_PATH), (30, 30))

    def __init__(self):
        super().__init__()
        self.image = Crosshair.CROSSHAIR
        self.rect = self.image.get_rect()
