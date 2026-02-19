import pygame as pg
from pygame.locals import *
import math

from Game import Game, GameMode
from Window import Window, DisplayedWindow


def eventHandler(window):
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        match window.displayedWindow:
            case DisplayedWindow.MAIN_MENU:
                window.updateMainMenu(event)
            case DisplayedWindow.GAME_SCENE:
                window.updateGameScene(event)
            case DisplayedWindow.SETTINGS:
                window.updateSettingsMenu(event)


def main():
    game = Game()
    window = Window(game)

    # Main game loop
    running = True
    while running:
        eventHandler(window)
        window.refreshDisplay()
        pg.time.Clock().tick(window.fps)


if __name__ == "__main__":
    pg.init() # TODO: here or at the beginning of main()?
    main()