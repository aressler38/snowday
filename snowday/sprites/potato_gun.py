import pkg_resources

import pygame
from pygame.math import Vector2
import pygame.mixer
import pygame.sprite
import pygame.image
import pygame.transform

from snowday.sprites.potato import Potato
from snowday.sound import Sound


class PotatoGun(pygame.sprite.Sprite):
    def __init__(self, pivot: Vector2):
        super().__init__()
        pth = pkg_resources.resource_filename(
            "snowday", "assets/sprites/potato_gun.png"
        )
        surface = pygame.image.load(pth)
        rect = surface.get_rect()
        factor = 4

        # We put potato sprites in a group so we can detect collisions.
        self.potatoes = pygame.sprite.Group()
        self.potato_speed = 0.0125

        self.pivot = pivot
        self.original = pygame.transform.scale(
            surface, (int(rect.width / factor), int(rect.height / factor))
        )
        self.original_rect = self.original.get_rect()
        self.original_rect.center = (pivot.x, pivot.y - self.original_rect.height / 2)
        self.original_center_vec = Vector2(self.pivot - self.original_rect.center)
        self.image = self.original
        self.rect = self.image.get_rect()
        # I'll used these to know where to launch the potatoes.
        # I'll update them in the rotate method.
        self.angle = 0
        self.center = self.rect.center
        self.direction = self.original_center_vec.rotate(self.angle)
        self.muzzle = Vector2(0, 0)
        self.update_muzzle()

    def update_muzzle(self):
        """
        The muzzle is the tip of the barrel where the potato exits.
        """
        floating_tip = 2 * self.direction
        self.muzzle = Vector2(
            floating_tip.x + self.pivot.x, self.pivot.y - floating_tip.y
        )

    def rotate(self, angle: float):
        """
        Rotate the potato gun about the pivot point.
        """
        # TODO: If I was smart, then I'd position the original image such that I wouldn't need
        # to rotate two vectors. I should just be able to rotate the one vector.
        rotated_image = pygame.transform.rotate(self.original, angle)
        self.angle = angle
        self.direction = self.original_center_vec.rotate(self.angle)
        self.center = (self.direction.x + self.pivot.x, self.pivot.y - self.direction.y)
        self.rect = rotated_image.get_rect(center=self.center)
        self.image = rotated_image
        self.update_muzzle()

    def shoot_potato(self):
        """
        Fire!!!
        """
        potato = Potato(self.direction, self.muzzle, self.potato_speed)
        self.potatoes.add(potato)
        Sound.SHOOT_SFX.play()
        print("potato")
