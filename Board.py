import pygame as pg
from pygame.locals import *
from enum import Enum

from ThemeManager import ThemeManager


class BoardParameters(Enum):
    BOARD_SIZE = 722
    BOARD_Y_OFFSET = 150
    NUM_CASE = 19
    CASE_SIZE = BOARD_SIZE // NUM_CASE
    BOARD_BORDER_SIZE = BOARD_SIZE - CASE_SIZE


class Board:
    def __init__(self):
        self.boardState = None
        self.themeManager = None
        self.color = (0, 0, 0)
        self.lineWidth = 2
        self.circleRadius = 7


    def _boardOrigin(self, window):
        return (
            window.size[0] // 2 - BoardParameters.BOARD_SIZE.value // 2,
            BoardParameters.BOARD_Y_OFFSET.value
            )


    def _boardBorderOrigin(self, window):
        return (
            self._boardOrigin(window)[0] + (BoardParameters.CASE_SIZE.value // 2),
            self._boardOrigin(window)[1] + (BoardParameters.CASE_SIZE.value // 2)
            )


    def getIndexFromPos(self, window, pos: tuple):
        boardOrigin = self._boardOrigin(window)
        x_rel = pos[0] - boardOrigin[0]
        y_rel = pos[1] - boardOrigin[1]
        if 0 <= x_rel < BoardParameters.BOARD_SIZE.value and 0 <= y_rel < BoardParameters.BOARD_SIZE.value:
            col = int(x_rel // BoardParameters.CASE_SIZE.value)
            row = int(y_rel // BoardParameters.CASE_SIZE.value)
            return (row, col)
        return (None, None)


    def _getPosFromIndex(self, row: int, col: int, window):
        boardBorderOrigin = self._boardBorderOrigin(window)
        x = boardBorderOrigin[0] + col * BoardParameters.CASE_SIZE.value
        y = boardBorderOrigin[1] + row * BoardParameters.CASE_SIZE.value
        return (x, y)


    def _drawGrid(self, window, color, lineWidth):
        for i in range(BoardParameters.NUM_CASE.value):
            # vertical lines
            startPos = (
                self._boardBorderOrigin(window)[0] + i * BoardParameters.CASE_SIZE.value - 1,
                self._boardBorderOrigin(window)[1] - 1
                )
            endPos = (
                self._boardBorderOrigin(window)[0] + i * BoardParameters.CASE_SIZE.value - 1,
                self._boardBorderOrigin(window)[1] + BoardParameters.BOARD_BORDER_SIZE.value - 1
                )
            pg.draw.line(window.display, color, startPos, endPos, lineWidth)

            # horizontal lines
            startPos = (
                self._boardBorderOrigin(window)[0] - 1,
                self._boardBorderOrigin(window)[1] + i * BoardParameters.CASE_SIZE.value - 1
                )
            endPos = (
                self._boardBorderOrigin(window)[0] + BoardParameters.BOARD_BORDER_SIZE.value - 1,
                self._boardBorderOrigin(window)[1] + i * BoardParameters.CASE_SIZE.value - 1
                )
            pg.draw.line(window.display, color, startPos, endPos, lineWidth)


    def _drawStarPoints(self, window, color, circleRadius):
        starPoints = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
    
        for point in starPoints:
            center = (
                self._boardBorderOrigin(window)[0] + point[0] * BoardParameters.CASE_SIZE.value,
                self._boardBorderOrigin(window)[1] + point[1] * BoardParameters.CASE_SIZE.value
                )
            pg.draw.circle(window.display, color, center, circleRadius)


    def _drawPieces(self, window):
        self.boardState = window.game.boardState

        for row in range(BoardParameters.NUM_CASE.value):
            for col in range(BoardParameters.NUM_CASE.value):
                if self.boardState[row][col] != 0:
                    # TODO: replace with custom piece images from theme manager
                    pos = self._getPosFromIndex(row, col, window)
                    color = (0, 0, 0) if self.boardState[row][col] == 1 else (255, 255, 255)
                    pg.draw.circle(window.display, color, pos, BoardParameters.CASE_SIZE.value // 2 - 2)


    def draw(self, window):
        self.color = window.themeManager.getBoardColor()

        self._drawGrid(window, self.color, self.lineWidth)
        self._drawStarPoints(window, self.color, self.circleRadius)
        self._drawPieces(window)
