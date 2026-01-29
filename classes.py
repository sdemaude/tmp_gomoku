import pygame as pg
from pygame.locals import *
import math

pg.init()

class PlayerIcon:
    def __init__(self, image_path, position, size, playerIndex=0):
        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self.originalPosition = position
        self.position = position
        self.playerIndex = playerIndex
    
    def draw(self, surface):
        surface.blit(self.image, self.position)

    def animate(self, surface):
        self.position = (self.originalPosition[0], self.originalPosition[1] + 10 * math.sin(pg.time.get_ticks() / 200))
        self.draw(surface)


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


class SoundEffects:
    def __init__(self):
        self.active = True
        self.sounds = {
            "pop": pg.mixer.Sound("assets/sound/pop_sound.mp3")}

    def play_sound(self, name):
        if name in self.sounds and self.active:
            self.sounds[name].play()

    def toggle(self):
        self.active = not self.active


class Case:
    def __init__(self, position, size, row, col):
        self.position = position
        self.size = size
        self.occupied_by = None
        self.rect = pg.Rect(position[0], position[1], size[0], size[1])
        self.on_hover = False

    def draw(self, surface):
        if self.on_hover:
            pg.draw.rect(surface, (200, 200, 200), self.rect, 3)

    def on_case(self, pos):
        return self.rect.collidepoint(pos)

    '''
    def on_click(self):
        if self.callback:
            self.callback(self)
    '''

    def update(self, event):
        '''
        if event.type == MOUSEBUTTONDOWN:
            if self.on_case(event.pos):
                self.on_click()
        '''
        if event.type == MOUSEMOTION:
            if self.on_case(event.pos):
                self.on_hover = True
            else:
                self.on_hover = False

'''
class Board:
    def __init__(self, size, case_size):
'''







#class AI:
#class Game:

#class Piece:
#class Player:

#class GameState:
#class Scoreboard:
#class Timer:

#class Settings:
#class Menu: