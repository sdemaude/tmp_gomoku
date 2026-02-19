import pygame as pg
from pygame.locals import *
from enum import Enum

class GameMode(Enum):
    PVP = 1
    PVE = 2

from Board import BoardParameters

class Game:
    def __init__(self):
        self.activePlayer = 1               # 1: Player 1, 2: Player 2
        self.mode = None                    # GameMode.PVP or GameMode.PVE
        self.currentScore = {1: 0, 2: 0}
        self.timerP1 = 0
        self.timerP2 = 0

        self.boardState = [[0 for _ in range(BoardParameters.NUM_CASE.value)] for _ in range(BoardParameters.NUM_CASE.value)] # 0: empty, 1: player1 piece, 2: player2 piece


    def init(self, gameMode: GameMode):
        self.activePlayer = 1
        self.mode = gameMode
        self.currentScore = {1: 0, 2: 0}
        self.boardState = [[0 for _ in range(BoardParameters.NUM_CASE.value)] for _ in range(BoardParameters.NUM_CASE.value)]


    def placePiece(self, row: int, col: int):
        self.boardState[row][col] = self.activePlayer


    def capturePieces(self, row: int, col: int):
        # check in all 8 directions for capture patterns
        # if a capture is detected, remove the captured pieces and update the score
        pass


    def checkWinCondition(self, row: int, col: int):
        # check in all 8 directions for 5 in a row
        # if 5 in a row is detected, return True for win condition
        pass


    def checkTieCondition(self):
        # check if the board is full
        if any(0 in row for row in self.boardState):
            return False
        return True


    def checkCaptureCondition(self, row: int, col: int):
        # check if the last move resulted in a capture
        pass


    def checkValidMove(self, row: int, col: int):
        # check if the move is valid according to the game rules (e.g., not placing on an occupied space, not violating opening rules)
        if self.boardState[row][col] != 0:
            return False
        return True


    def handleMove(self, row: int, col: int):
        if self.checkValidMove(row, col):
            self.placePiece(row, col)
            #self.history.append((row, col, self.activePlayer))
            '''
            if self.checkCaptureCondition(row, col):
                self.capturePieces(row, col)
                # update score

            if self.checkWinCondition(row, col):
                # handle win condition
                pass
            elif self.checkTieCondition():
                winner = max(self.currentScore, key=self.currentScore.get)
                # handle tie condition
                pass
            '''
            self.activePlayer = 2 if self.activePlayer == 1 else 1


    def update(self, event, window):
        # start timer for active player
        if event.type == MOUSEBUTTONDOWN:
            gameMove = window.board.getIndexFromPos(window, event.pos)
            if gameMove[0] is not None and gameMove[1] is not None:
                # stop timer for active player -> what happens if the move is invalid? should the timer continue until a valid move is made?
                self.handleMove(gameMove[0], gameMove[1])

        # where to put this V?
        #if game.mode == GameMode.PVE and game.activePlayer == 2:
            # start AI timer
            # gameMove = getAIMove()
            # stop AI timer
            #self.handleMove(gameMove[0], gameMove[1])