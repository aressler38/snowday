"""
This is the game class
"""
import sys
import math
import pygame
import pygame.time
from pygame.math import Vector2
import pygame.sprite
import pygame.mouse
import pygame.font
from snowday.sound import Sound
from snowday.bgm import Bgm
from snowday.sprites.snowflake import Snowflake
from snowday.sprites.potato_gun import PotatoGun


class Game:
    HEIGHT = 700
    WIDTH = 900
    ACC = 0.5
    FRIC = -0.12
    FPS = 22
    SNOWFLAKE_FACTOR = 1000

    def __init__(self, **kwargs):
        """ Setup stuff in here """
        pygame.init()
        caption = kwargs.get("caption", "Game")
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.displaysurface = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.bgm = Bgm()
        self.level = 1
        self.last_spawn_time = -1
        self.score = {
            "hits": 0,
            "melts": 0,
        }
        # Keep scores on a score board.
        self.scoreboard = pygame.Surface((300, 100))
        self.scoreboard_rect = pygame.Rect(Game.WIDTH / 2, 0, Game.WIDTH / 2, 50)
        self.myfont = pygame.font.SysFont("Console", 28)

    def get_gun_angle(self):
        """
        Calculate the angle the potato gun should point based on the mouse cursor.
        """
        vec2 = pygame.mouse.get_pos()
        y = Game.HEIGHT - vec2[1]
        x = vec2[0] - Game.WIDTH / 2
        angle = int(math.atan2(y, x) * 180 / math.pi) - 90
        return angle

    def render_scoreboard(self):
        """ show the score and level """
        self.scoreboard.fill((55, 55, 55))
        self.displaysurface.blit(self.scoreboard, self.scoreboard_rect)
        self.displaysurface.blit(
            self.myfont.render(
                "Hits: %s" % self.score["hits"],
                True,
                "green",
            ),
            (self.scoreboard_rect.left, self.scoreboard_rect.top + 0),
        )
        self.displaysurface.blit(
            self.myfont.render(
                "Melts: %s" % self.score["melts"],
                True,
                "red",
            ),
            (self.scoreboard_rect.left, self.scoreboard_rect.top + 30),
        )
        self.displaysurface.blit(
            self.myfont.render(
                "Level: %s" % self.level,
                True,
                "orange",
            ),
            (self.scoreboard_rect.left, self.scoreboard_rect.top + 60),
        )

    def run(self):
        """ Run the game loop """
        self.bgm.play()

        snowflakes = pygame.sprite.Group()

        platform = pygame.sprite.Sprite()
        platform.rect = pygame.Rect(0, 40, Game.WIDTH, 50)
        platform.rect.bottom = Game.HEIGHT
        platform.rect.width = Game.WIDTH
        platform.image = pygame.Surface([platform.rect.width, platform.rect.height])
        platform.image.fill((255, 255, 255))

        potato_gun = PotatoGun(Vector2(Game.WIDTH / 2, Game.HEIGHT))

        # Keep track of when the player finishes clicking a mouse button.
        click_start = False

        # Record the time since last levelup.
        last_levelup = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting")
                    pygame.quit()
                    sys.exit()

            # Get the current time.
            now = pygame.time.get_ticks()

            # See if it's time to levelup yet.
            if now - last_levelup > 15000 * self.level:
                self.level += 1
                last_levelup = now

            # Draw a black background.
            self.displaysurface.fill((0, 0, 0))
            # Draw the ground.
            self.displaysurface.blit(platform.image, platform.rect)

            # Draw the scoreboard
            self.render_scoreboard()

            # Spawn snowflakes.
            if now - self.last_spawn_time > (Game.SNOWFLAKE_FACTOR / self.level):
                snowflakes.add(Snowflake(self.displaysurface))
                self.last_spawn_time = now

            # Update the snowflakes sprite group causing them to fall.
            snowflakes.update()
            # Check if the snowflake hit the ground.
            for snowflake in pygame.sprite.spritecollide(platform, snowflakes, True):
                print("melt")
                self.score["melts"] += 1
                snowflake = Snowflake(self.displaysurface)
                Sound.MELT_SFX.play()
                snowflakes.add(snowflake)
            # Draw the snowflakes that didn't hit the ground.
            snowflakes.draw(self.displaysurface)

            # Calculate the potato gun angle based on the mouse cursor.
            angle = self.get_gun_angle()
            # Aim the gun.
            potato_gun.rotate(angle)
            # Draw the potato gun
            self.displaysurface.blit(potato_gun.image, potato_gun.rect)

            # See if the player finished clicking a shoot button.
            for mouse_btn in pygame.mouse.get_pressed(3):
                if mouse_btn:
                    click_start = True
                    break
                if click_start:
                    # You can change the speed here
                    potato_gun.shoot_potato(potato_gun.potato_speed)
                    click_start = False

            # Show the potatoes flying!
            potato_gun.potatoes.update()
            potato_gun.potatoes.draw(self.displaysurface)

            # See if any potatoes fried some snowflakes.
            # Note: there is a groupcollide() function that pygame provides, but
            # I think it is overkill, and it has the potential to over measure in this game.
            for potato in potato_gun.potatoes:
                for snowflake in pygame.sprite.spritecollide(potato, snowflakes, True):
                    print("shot that snowflake!")
                    self.score["hits"] += 1
                    Sound.HIT_SFX.play()

            # Update the display and clock.
            pygame.display.update()
            self.clock.tick(Game.FPS)
