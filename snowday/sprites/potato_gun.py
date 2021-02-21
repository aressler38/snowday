from typing import Tuple
import pkg_resources

import pygame
import pygame.sprite
import pygame.image
import pygame.transform


class PotatoGun(pygame.sprite.Sprite):

    def __init__(self, center: Tuple):
        super().__init__()
        pth = pkg_resources.resource_filename(
            'snowday',
            'assets/sprites/potato_gun.png')
        surface = pygame.image.load(pth)
        rect = surface.get_rect()
        factor = 4
        self.original = pygame.transform.scale(surface, (int(rect.width / factor), int(rect.height / factor)))
        self.original.get_rect().center = center
        self.image = self.original
        self.rect = self.image.get_rect()
        self.angle = 0

    def rotate(self, angle: float, pivot):
        self.angle = angle
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect.center = pivot
