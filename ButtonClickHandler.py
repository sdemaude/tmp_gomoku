import pygame as pg
from pygame.locals import *

from ThemeManager import ThemeManager
import themes

class ButtonClickHandler:
    def __init__(self, game, window, soundEffects, musicPlayer):
        self.game = game
        self.window = window
        self.themeManager = window.themeManager
        self.soundEffects = soundEffects
        self.musicPlayer = musicPlayer


    def home_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.game.displayedWindow = 0


    def exit_button_click(self, button):
        self.soundEffects.play_sound("pop")
        pg.quit()
        exit()


    def music_button_click(self, button):
        self.soundEffects.play_sound("pop")
        if button.active:
            self.musicPlayer.unpause()
        else:
            self.musicPlayer.pause()


    def sound_button_click(self, button):
        self.soundEffects.toggle()
        self.soundEffects.play_sound("pop")


    def play_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.game.displayedWindow = 1


    def setting_button_click(self, button):
        self.soundEffects.play_sound("pop")
        match self.game.displayedWindow:
            case 0:
                self.game.displayedWindow = 2
            case 2:
                self.game.displayedWindow = 0


    def pvp_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.game.mode = "pvp"
        self.game.displayedWindow = 1


    def pve_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.game.mode = "pve"
        self.game.displayedWindow = 1


    def theme1_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("classic")


    def theme2_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("crystal")


    def theme3_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("classic")


    def theme4_button_click(self, button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("crystal")