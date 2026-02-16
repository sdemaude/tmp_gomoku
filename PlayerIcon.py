import pygame as pg
from pygame.locals import *
import math


class PlayerIcon:
    def __init__(self, themeManager, game, position, size, playerId):
        self.game = game
        self.size = size
        self.themeManager = themeManager
        self.originalPosition = position
        self.position = position
        self.playerId = playerId

    def image(self):
        image = self.themeManager.getPlayerIcon(self.playerId, self.game.mode)
        return pg.transform.scale(image, self.size)
    
    def draw(self, surface):
        if self.game.activePlayer == self.playerId:
            self.animate(surface)
            surface.blit(self.image(), self.position)
        else: 
            surface.blit(self.image(), self.originalPosition)

    def animate(self, surface):
        self.position = (self.originalPosition[0], self.originalPosition[1] + 20 * math.sin(pg.time.get_ticks() / 200))