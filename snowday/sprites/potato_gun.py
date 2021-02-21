from typing import Tuple
import pkg_resources

import pygame
from pygame.math import Vector2
import pygame.sprite
import pygame.image
import pygame.transform


class PotatoGun(pygame.sprite.Sprite):

    def __init__(self, pivot: Vector2):
        super().__init__()
        pth = pkg_resources.resource_filename(
            'snowday',
            'assets/sprites/potato_gun.png')
        surface = pygame.image.load(pth)
        rect = surface.get_rect()
        factor = 4
        self.potatoes = pygame.sprite.Group()
        self.pivot = pivot
        self.original = pygame.transform.scale(surface, (int(rect.width / factor), int(rect.height / factor)))
        self.original_rect = self.original.get_rect()
        self.original_rect.center = (pivot.x, pivot.y - self.original_rect.height / 2)
        self.original_center_vec = Vector2(self.pivot - self.original_rect.center)
        print(self.original_rect.center)
        self.image = self.original
        self.rect = self.image.get_rect()
        self.angle = 0


    def rotate(self, angle: float):
        """
        Rotate the potato gun about the pivot point.
        """
        # TODO: If I was smart, then I'd position the original image such that I wouldn't need
        # to rotate two vectors. I should just be able to rotate the one vector.
        rotated_image = pygame.transform.rotate(self.original, angle)
        floating_center = self.original_center_vec.rotate(angle)
        center = (floating_center.x + self.pivot.x, self.pivot.y - floating_center.y)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image
        self.angle = angle

    def shoot_potato(self):
        """
        Fire!!!
        """
        print('potato')
