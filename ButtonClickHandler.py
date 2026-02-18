import pygame as pg
from pygame.locals import *

from Game import Game
from Window import DisplayedWindow
from Button import Button, ToggleButton
import themes
from ThemeManager import ThemeManager


class ButtonClickHandler:
    def __init__(self, game: Game, window):
        self.game = game
        self.window = window
        self.themeManager = window.themeManager
        self.soundEffects = window.soundEffects
        self.musicPlayer = window.musicPlayer

    def home_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.displayedWindow = DisplayedWindow.MAIN_MENU


    def exit_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        pg.quit()
        exit()


    def music_button_click(self, button: ToggleButton):
        self.soundEffects.play_sound("pop")
        if button.active:
            self.musicPlayer.unpause()
        else:
            self.musicPlayer.pause()


    def sound_button_click(self, button: ToggleButton):
        self.soundEffects.toggle()
        self.soundEffects.play_sound("pop")


    def play_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.displayedWindow = DisplayedWindow.GAME_SCENE


    def setting_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        match self.window.displayedWindow:
            case DisplayedWindow.MAIN_MENU:
                self.window.displayedWindow = DisplayedWindow.SETTINGS
            case DisplayedWindow.SETTINGS:
                self.window.displayedWindow = DisplayedWindow.MAIN_MENU


    def pvp_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.game.mode = "pvp"
        self.window.displayedWindow = DisplayedWindow.GAME_SCENE


    def pve_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.game.mode = "pve"
        self.window.displayedWindow = DisplayedWindow.GAME_SCENE


    def theme1_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("classic")


    def theme2_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("crystal")


    def theme3_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("classic")


    def theme4_button_click(self, button: Button):
        self.soundEffects.play_sound("pop")
        self.window.themeManager.setTheme("crystal")