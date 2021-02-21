import math
import pkg_resources

import pygame
from pygame.math import Vector2
import pygame.sprite
import pygame.image
import pygame.transform
import pygame.time


class Potato(pygame.sprite.Sprite):

    # All potatoes are the same, so we load them in the static area.
    POTATO_IMAGE_PATH = pkg_resources.resource_filename(
        "snowday", "assets/sprites/potato.png"
    )

    # Make the potato sprite about 15x15 pixels.
    POTATO = pygame.transform.scale(pygame.image.load(POTATO_IMAGE_PATH), (15, 15))

    MAX_LIFE = 5000  # No potato should last longer than 5 seconds.

    def __init__(self, direction: Vector2, start: Vector2, speed=1.0):
        super().__init__()
        self.direction = direction.normalize()
        self.direction.y *= -1  # Y-axis is inverted... + is down, - is up
        self.start = start
        self.bday = pygame.time.get_ticks()
        self.speed = speed
        self.image = pygame.transform.rotate(
            Potato.POTATO, math.atan2(direction.y, direction.x)
        )
        self.rect = self.image.get_rect(center=self.start)

    def update(self):
        now = pygame.time.get_ticks()
        time_delta = now - self.bday
        self.rect.center = (time_delta * self.speed * self.direction) + Vector2(
            self.rect.center
        )
        if now - self.bday > Potato.MAX_LIFE:
            self.kill()
