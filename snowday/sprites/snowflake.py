import enum
import random
import pkg_resources

import pygame
import pygame.time
import pygame.sprite
import pygame.image
import pygame.transform


class Snowflake(pygame.sprite.Sprite):
    MAX_LIFE = 20 * 1000  # 20 seconds

    class Type(enum.Enum):
        drop = 1
        diagonal_left = 2
        diagonal_right = 3

    def __init__(self, displaysurface: pygame.Surface):
        super().__init__()
        pth = pkg_resources.resource_filename(
            "snowday", "assets/sprites/snowflake%d.png" % random.randint(1, 9)
        )
        self.displaysurface = displaysurface
        self.size = random.randint(34, 40)
        self.original = pygame.transform.scale(
            pygame.image.load(pth), (self.size, self.size)
        )
        self.image = self.original
        self.rect = self.image.get_rect()
        self.angle = 0
        self.rotate_speed = 10
        self.bday = pygame.time.get_ticks()
        self.now = self.bday
        self.type = random.choice([kind for kind in Snowflake.Type])
        self.updated = False

    def rotate(self):
        self.angle = (self.angle + self.rotate_speed) % 360
        self.image = pygame.transform.rotate(self.original, self.angle)

    def update(self):
        self.now = pygame.time.get_ticks()
        self.rotate()

        # self.rect = self.image.get_rect(center=center)
        if self.type == Snowflake.Type.drop:
            self.random_drop()
        elif self.type == Snowflake.Type.diagonal_left:
            self.diagonal_left()
        elif self.type == Snowflake.Type.diagonal_right:
            self.diagonal_right()
        else:
            raise Exception("you forgot to add the function here")
        # TODO: make more interesting ways to drop the snowflakes
        # like with sinewaves and other types of functions.
        self.updated = True

        # In case it floated away, then kill it.
        if self.now - self.bday > Snowflake.MAX_LIFE:
            self.kill()

    def random_drop(self):
        """
        Pick a spot on the x-axis and then let it fall down.
        """
        if self.updated:
            self.rect.centery += 10
        else:
            self.rect.centerx = random.randrange(
                self.size, self.displaysurface.get_rect().width
            )

    def diagonal_left(self):
        """
        Go from top left to bottom right.
        """
        fall_time = 3000  # it's milliseconds

        rect = self.displaysurface.get_rect()
        if not self.updated:
            self.rect.centerx = 0

        ratio = (self.now - self.bday) / (1.0 * fall_time)
        x = ratio * rect.width
        y = ratio * rect.height
        self.rect.center = (x, y)

    def diagonal_right(self):
        """
        Go from top right to bottom left.
        """
        fall_time = 2300  # it's milliseconds

        rect = self.displaysurface.get_rect()
        if not self.updated:
            self.rect.centerx = rect.width

        ratio = (self.now - self.bday) / (1.0 * fall_time)
        x = (1.0 - ratio) * rect.width
        y = ratio * rect.height
        self.rect.center = (x, y)
