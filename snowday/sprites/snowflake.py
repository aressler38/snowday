import random
import pkg_resources

import pygame
import pygame.sprite
import pygame.image
import pygame.transform


class Snowflake(pygame.sprite.Sprite):

    def __init__(self, size = 40):
        super().__init__()
        pth = pkg_resources.resource_filename(
            'snowday',
            'assets/sprites/snowflake%d.png' % random.randint(1, 9))
        self.size = size
        self.original = pygame.transform.scale(pygame.image.load(pth), (self.size, self.size))
        self.image = self.original
        self.rect = self.image.get_rect()
        self.angle = 0
        self.rotate_speed = 10

    def resize(self, size: int):
        self.size = size
        return pygame.transform.scale(self.original, (self.size, self.size))

    def update(self):
        self.angle = (self.angle + self.rotate_speed) % 360
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect.centery += self.rotate_speed
        #self.rect = self.image.get_rect(center=center)
