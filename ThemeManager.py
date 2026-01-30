import pygame as pg
from pygame.locals import *

class ThemeManager:
    def __init__(self, themes, default="classic"):
        self.themes = themes
        self.current = None
        self.images = {}
        self.set_theme(default)

    def set_theme(self, name):
        self.current = self.themes[name]
        self.fontName = self.current["font"]
        self._load_images()
        self._load_music()

    def _load_images(self):
        self.images.clear()
        for key, path in self.current["images"].items():
            self.images[key] = pg.image.load(path).convert_alpha()

    def _load_music(self):
        pg.mixer.music.load(self.current["music"])
        pg.mixer.music.play(-1)