import pygame as pg
from pygame.locals import *
import math

from Game import Game, GameMode
from Window import Window, DisplayedWindow


def updateMainMenu(window: Window, event: pg.event.Event):
    window.pvpButton.update(event)
    window.pveButton.update(event)
    window.settingButton.update(event)
    window.exitButton.update(event)


def updateGameScene(window: Window, event: pg.event.Event, game: Game):
    window.homeButton.update(event)
    window.exitButton.update(event)

    if event.type == MOUSEBUTTONDOWN:
        game_move = game.getIndexFromPos(window, event.pos)
        if game_move[0] is not None and game_move[1] is not None:
            # check if the move is valid
            if game.placePiece(game_move[0], game_move[1]):
                # soundEffects.playPieceSound()
                # check for win/tie condition or capture
                game.activePlayer = 2 if game.activePlayer == 1 else 1

            #if game.mode == GameMode.PVE and game.activePlayer == 2:
                # start AI timer
                # get AI move
                # stop AI timer
                # place AI move
                # update history
                # check for win/tie condition or capture
                #game.activePlayer = 1
                # restart the loop to wait for player move


def updateSettingsMenu(window: Window, event: pg.event.Event):
    window.homeButton.update(event)
    window.settingButton.update(event)
    window.musicButton.update(event)
    window.soundButton.update(event)
    window.theme1Button.update(event)
    window.theme2Button.update(event)
    window.theme3Button.update(event)
    window.theme4Button.update(event)
    window.homeButton.update(event)
    window.exitButton.update(event)


def main():
    game = Game()
    window = Window(game)

    # Main game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
            match window.displayedWindow:
                case DisplayedWindow.MAIN_MENU:
                    updateMainMenu(window, event)
                case DisplayedWindow.GAME_SCENE:
                    updateGameScene(window, event, game)
                case DisplayedWindow.SETTINGS:
                    updateSettingsMenu(window, event)

        match window.displayedWindow:
            case DisplayedWindow.MAIN_MENU:
                window.drawMainMenu()
            case DisplayedWindow.GAME_SCENE:
                window.drawGameScene()
            case DisplayedWindow.SETTINGS:
                window.drawSettingsMenu()

        pg.time.Clock().tick(window.fps)


if __name__ == "__main__":
    pg.init()
    main()