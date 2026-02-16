import pygame as pg
from pygame.locals import *


class ThemeManager:
    def __init__(self, themes, window, default="classic"):
        self.themes = themes
        self.window = window
        self.current = None
        self._images = {}
        self.setTheme(default)


    def getPlayerIcon(self, playerId, gamemode):
        if gamemode == "pvp":
            return self._images["icon_player1"] if playerId == 1 else self._images["icon_player2"]
        elif gamemode == "pve":
            return self._images["icon_player1"] if playerId == 1 else self._images["icon_playerIA"]
        else:
            raise ValueError("Invalid game mode")


    def getBackground(self):
        return self._images.get("background")


    def getBoardColor(self):
        return self.current["colors"]["grid"]


    def setTheme(self, name):
        self.current = self.themes[name]
        self.fontName = self.current["font"]
        self._loadImages()
        #self._load_music()


    def _loadImages(self):
        self._images.clear()
        for key, path in self.current["images"].items():
            self._images[key] = pg.image.load(path).convert_alpha()


    '''def _load_music(self):
        pg.mixer.music.load(self.current["music"])
        pg.mixer.music.play(-1)'''