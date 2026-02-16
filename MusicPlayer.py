import pygame as pg
from pygame.locals import *


class MusicPlayer:
    def __init__(self, music_file):
        pg.mixer.music.load(music_file)

    def play(self, loops=-1):
        pg.mixer.music.play(loops)

    def pause(self):
        pg.mixer.music.pause()

    def unpause(self):
        pg.mixer.music.unpause()

    def is_playing(self):
        return pg.mixer.music.get_busy()

    '''
    def turn_volume_up(self, increment=0.1):
        current_volume = pg.mixer.music.get_volume()
        new_volume = min(1.0, current_volume + increment)
        pg.mixer.music.set_volume(new_volume)
    
    def turn_volume_down(self, decrement=0.1):
        current_volume = pg.mixer.music.get_volume()
        new_volume = max(0.0, current_volume - decrement)
        pg.mixer.music.set_volume(new_volume)
    '''