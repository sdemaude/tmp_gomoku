import pygame as pg
from pygame.locals import *
from enum import Enum

class GameMode(Enum):
    PVP = 1
    PVE = 2

from Board import BoardParam

class Game:
    def __init__(self):
        self.activePlayer = 1               # 1: Player 1, 2: Player 2
        self.mode = None                    # GameMode.PVP or GameMode.PVE
        self.currentScore = {1: 0, 2: 0}
        self.timerP1 = 0
        self.timerP2 = 0

        self.boardState = [[0 for _ in range(BoardParam.NUM_CASE)] for _ in range(BoardParam.NUM_CASE)] # 0: empty, 1: player1 piece, 2: player2 piece


    def _placePiece(self, row: int, col: int):
        self.boardState[row][col] = self.activePlayer


    def _capturePieces(self, row: int, col: int):
        # if a capture is detected, remove the captured pieces
        # look for patterns like: player piece - opponent piece - opponent piece - player piece (depth of 4 in a row)
        pass


    def _checkFiveInARow(self, row: int, col: int):
        # check if the last move resulted in 5 pieces in a row for the active player
        # check horizontally, vertically, and both diagonals
        pass


    def _checkWinCondition(self, row: int, col: int):
        if self._checkFiveInARow(row, col) or self.currentScore[self.activePlayer] >= 10:
            return True
        return False


    def _checkTieCondition(self):
        # check if the board is full
        if any(0 in row for row in self.boardState):
            return False
        return True


    def _checkCaptureCondition(self, row: int, col: int):
        # check if the last move resulted in a capture
        pass


    def _checkValidMove(self, row: int, col: int):
        # check if the move is valid according to the game rules (e.g., not placing on an occupied space, not violating opening rules)
        if self.boardState[row][col] != 0:
            return False
        return True


    def _handleMove(self, row: int, col: int):
        if self._checkValidMove(row, col):
            self._placePiece(row, col)
            #self.history.append((row, col, self.activePlayer))
            '''
            if self._checkCaptureCondition(row, col):
                self._capturePieces(row, col)
                if self.activePlayer == 1:
                    self.currentScore[1] += 2
                else:
                    self.currentScore[2] += 2

            if self._checkWinCondition(row, col):
                # handle win condition
                pass
            elif self._checkTieCondition():
                winner = max(self.currentScore, key=self.currentScore.get)
                # handle tie condition
                pass
            '''
            self.activePlayer = 2 if self.activePlayer == 1 else 1


# Public methods
    def init(self, gameMode: GameMode):
        self.activePlayer = 1
        self.mode = gameMode
        self.currentScore = {1: 0, 2: 0}
        self.boardState = [[0 for _ in range(BoardParam.NUM_CASE)] for _ in range(BoardParam.NUM_CASE)]


    def update(self, event: pg.event.Event, window):
        # start timer for active player
        if event.type == MOUSEBUTTONDOWN:
            gameMove = window.board.getIndexFromPos(window, event.pos)
            if gameMove[0] is not None and gameMove[1] is not None:
                # stop timer for active player -> what happens if the move is invalid? should the timer continue until a valid move is made?
                self._handleMove(gameMove[0], gameMove[1])

        # where to put this V? -> ?
        #if game.mode == GameMode.PVE and game.activePlayer == 2:
            # start AI timer
            # gameMove = getAIMove()
            # stop AI timer
            #self._handleMove(gameMove[0], gameMove[1])