import pygame as pg
from pygame.locals import *
from enum import Enum


class GameMode(Enum):
    PVP = 1
    PVE = 2


class Game:
    def __init__(self):
        self.activePlayer = 1               # 1: Player 1, 2: Player 2
        self.mode = None                    # GameMode.PVP or GameMode.PVE
        self.currentScore = {1: 0, 2: 0}
        self.boardSize = 722
        self.boardYOffset = 150
        self.numCase = 19
        self.caseSize = self.boardSize // self.numCase
        self.boardBorderSize = self.boardSize - self.caseSize

        self.boardState = [[0 for _ in range(self.numCase)] for _ in range(self.numCase)] # 0: empty, 1: player 1 piece, 2: player 2 piece


    def init(self, gameMode: GameMode):
        self.activePlayer = 1
        self.mode = gameMode
        self.currentScore = {1: 0, 2: 0}
        self.boardState = [[0 for _ in range(self.numCase)] for _ in range(self.numCase)]


    def boardOrigin(self, window):
        return (window.size[0] // 2 - self.boardSize // 2, self.boardYOffset)


    def boardBorderOrigin(self, window):
        return (self.boardOrigin(window)[0] + (self.caseSize // 2), self.boardOrigin(window)[1] + (self.caseSize // 2))


    def getIndexFromPos(self, window, pos: tuple):
        boardOrigin = self.boardOrigin(window)
        x_rel = pos[0] - boardOrigin[0]
        y_rel = pos[1] - boardOrigin[1]
        if 0 <= x_rel < self.boardSize and 0 <= y_rel < self.boardSize:
            col = int(x_rel // self.caseSize)
            row = int(y_rel // self.caseSize)
            return (row, col)
        return (None, None)


    def getPosFromIndex(self, row: int, col: int, window):
        boardBorderOrigin = self.boardBorderOrigin(window)
        x = boardBorderOrigin[0] + col * self.caseSize
        y = boardBorderOrigin[1] + row * self.caseSize
        return (x, y)


    def placePiece(self, row: int, col: int):
        if self.boardState[row][col] == 0:
            self.boardState[row][col] = self.activePlayer
            return True
        return False