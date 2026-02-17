import pygame as pg
from pygame.locals import *
import math

from Game import Game
from Window import Window

# delete later
from MusicPlayer import MusicPlayer
from SoundEffects import SoundEffects


def main():
    game = Game()
    window = Window(game)

    # delete later
    musicPlayer = MusicPlayer("assets/sound/background_music.mp3")
    musicPlayer.play()
    soundEffects = SoundEffects()
    window.setButtons(soundEffects, musicPlayer)
    window.drawMainMenu()

    # Main game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False

            match game.displayedWindow:
                case 0:
                    #window.playButton.update(event)
                    window.pvpButton.update(event)
                    window.pveButton.update(event)
                    window.settingButton.update(event)
                case 1:
                    window.homeButton.update(event)

                    if event.type == MOUSEBUTTONDOWN:
                        game_move = game.getIndexFromPos(window, event.pos)
                        if game_move[0] is not None and game_move[1] is not None:
                        # check if the move is valid
                            if game.placePiece(game_move[0], game_move[1]): # add sound effect when placing piece
                                #soundEffects.playPieceSound()
                                game.activePlayer = 2 if game.activePlayer == 1 else 1
                        # check for win/tie condition
                        # if AI mode, get AI move and repeat the above steps for AI move

                    # TODO: game logic
                    # check event in the game -> tie; win; switch player; invalid move; capture
                case 2:
                    window.settingButton.update(event)
                    window.musicButton.update(event)
                    window.soundButton.update(event)
                    window.theme1Button.update(event)
                    window.theme2Button.update(event)
                    window.theme3Button.update(event)
                    window.theme4Button.update(event)
            window.exitButton.update(event)

        match game.displayedWindow:
            case 0:
                window.drawMainMenu()
                game.reset()
            case 1:
                window.drawGameScene()
            case 2:
                window.drawSettingsMenu()

        pg.time.Clock().tick(window.fps)


if __name__ == "__main__":
    pg.init()
    main()