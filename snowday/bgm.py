"""
Bgm class for music.
"""

import pygame
import pygame.midi
import pkg_resources


class Bgm:

    DEFAULT = pkg_resources.resource_filename("snowday", "assets/midi/bwv-894.mid")

    def play(self, filename=DEFAULT):
        """
        Play the bgm file.
        """
        print("playing %s" % filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1, 0.0)

    def stop(self):
        """
        Stop the music.
        """
        pygame.mixer.music.stop()
