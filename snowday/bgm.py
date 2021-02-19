"""
Bgm class for music.
"""

import pygame
import pygame.midi
import os

class Bgm():

    DEFAULT=os.path.join(os.path.dirname(__file__), 'assets/midi/bwv-894.mid')

    def __init__(self):
        # mixer config
        freq = 44100    # audio CD quality
        bitsize = -16     # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024     # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(1.0)

    def play(self, filename=DEFAULT):
        """
        Play the bgm file.
        """
        print('playing %s' % filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1, 0.0)

    def stop(self):
        """
        Stop the music.
        """
        pygame.mixer.music.stop()
