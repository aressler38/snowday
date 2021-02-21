import pygame.mixer
import pkg_resources


class Sound:
    """
    mixer config
    """

    print("Setting up sound...")

    FREQ = 44100  # audio CD quality
    BITSIZE = -16  # unsigned 16 bit
    CHANNELS = 2  # 1 is mono, 2 is stereo
    BUFFER = 1024  # number of samples
    pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
    pygame.mixer.music.set_volume(1.0)

    SHOOT_SFX = pygame.mixer.Sound(
        pkg_resources.resource_filename("snowday", "assets/sfx/sfx1.mp3")
    )
    SHOOT_SFX.set_volume(0.7)
    HIT_SFX = pygame.mixer.Sound(
        pkg_resources.resource_filename("snowday", "assets/sfx/sfx2.mp3")
    )
    MELT_SFX = pygame.mixer.Sound(
        pkg_resources.resource_filename("snowday", "assets/sfx/sfx3.mp3")
    )
    MELT_SFX.set_volume(0.4)
