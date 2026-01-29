import pygame as pg
from pygame.locals import *
import classes
import math
from Button import Button, ToggleButton
from button_click import ButtonClickHandler

pg.init()

class Window:
    def __init__(self):
        self.size = (1600, 900)
        self.iconSize = 50
        self.fps = 30
        self.fontName = "Arial"


    def loadAssets(self, game):
        '''
        musicPlayer = classes.MusicPlayer("assets/sound/background_music.mp3")
        musicPlayer.play()
        soundEffects = classes.SoundEffects()
        '''
        self.player1Icon = classes.PlayerIcon("assets/image/pikachu.png", (self.size[0] // 2 - 300, 30), (100, 100))
        self.player2Icon = classes.PlayerIcon("assets/image/robot-head.png", (self.size[0] // 2 + 200, 30), (100, 100))


    def setButtons(self, game, soundEffects, musicPlayer):
        buttonClick = ButtonClickHandler(game, soundEffects, musicPlayer)

        self.exitButton = Button("assets/image/icon_exit.png", (self.size[0] - 60, 10), (self.iconSize, self.iconSize), buttonClick.exit_button_click)
        self.settingButton = Button("assets/image/icon_settings.png", (self.size[0] - 120, 10), (self.iconSize, self.iconSize), buttonClick.setting_button_click)
        self.homeButton = Button("assets/image/icon_home.png", (self.size[0] - 120, 10), (self.iconSize, self.iconSize), buttonClick.home_button_click)
        self.musicButton = ToggleButton("assets/image/icon_music_on.png", "assets/image/icon_music_off.png", (10, 10), (self.iconSize, self.iconSize), True, buttonClick.music_button_click)
        self.soundButton = ToggleButton("assets/image/icon_sound_on.png", "assets/image/icon_sound_off.png", (70, 10), (self.iconSize, self.iconSize), True, buttonClick.sound_button_click)
        self.playButton = Button("assets/image/button_play.png", (self.size[0] // 2 - 100, self.size[1] // 2 - 50), (100, 100), buttonClick.play_button_click)


    def drawSettingsMenu(self, Display):
        Display.fill((0x9A, 0x94, 0xBC))

        # display "Settings" title
        font = pg.font.SysFont(self.fontName, 100)
        title = font.render("Settings", True, (255, 255, 255))
        Display.blit(title, (self.size[0] // 2 - title.get_width() // 2, 100))

        self.musicButton.draw(Display)
        self.soundButton.draw(Display)

        self.settingButton.draw(Display)
        self.exitButton.draw(Display)
        pg.display.flip()


    def drawBoard(self, Display, game, color=(0, 0, 0)):
        # draw 19x19 grid
        board_origin = (self.size[0] // 2 - game.boardSizeGlobal // 2 + game.caseSize // 2, self.size[1] // 2 - game.boardSizeGlobal // 2.3 + game.caseSize // 2)
        for i in range(game.numCase):
            # vertical lines
            start_pos = (board_origin[0] + i * game.caseSize, board_origin[1])
            end_pos = (board_origin[0] + i * game.caseSize, board_origin[1] + game.boardSizeGlobal - game.caseSize)
            pg.draw.line(Display, color, start_pos, end_pos, 2)
            # horizontal lines
            start_pos = (board_origin[0], board_origin[1] + i * game.caseSize)
            end_pos = (board_origin[0] + game.boardSizeGlobal - game.caseSize, board_origin[1] + i * game.caseSize)
            pg.draw.line(Display, color, start_pos, end_pos, 2)
        
        # draw star points
        star_points = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
        for point in star_points:
            center = (board_origin[0] + point[0] * game.caseSize + 1, board_origin[1] + point[1] * game.caseSize + 1)
            pg.draw.circle(Display, color, center, 7)


    def drawGameScene(self, Display, game):
        Display.fill((0x9A, 0x94, 0xBC))
        self.drawBoard(Display, game)

        self.exitButton.draw(Display)
        self.homeButton.draw(Display)

        if game.activePlayer == 1:
            self.player1Icon.animate(Display)
            self.player2Icon.draw(Display)
        else:
            self.player1Icon.draw(Display)
            self.player2Icon.animate(Display)

        # print scores
        font = pg.font.SysFont(self.fontName, 90)
        score = font.render(f"{game.currentScore[1]} | {game.currentScore[2]}", True, (255, 255, 255))
        Display.blit(score, (self.size[0] // 2 - score.get_width() // 2, 30))

        pg.display.flip()


    def drawMainMenu(self, Display):
        Display.fill((0x9A, 0x94, 0xBC))

        self.exitButton.draw(Display)
        self.playButton.draw(Display)
        self.settingButton.draw(Display)

        pg.display.flip()


class Game:
    def __init__(self):
        self.displayedWindow = 0            # 0: Main Menu, 1: Game Scene, 2: Settings Menu
        self.activePlayer = 1               # 1: Player 1, 2: Player 2
        self.currentScore = {1: 0, 2: 0}
        self.gameMode = None                # "PVP" or "PVE"
        self.numCase = 19
        self.boardSizeGlobal = 722
        self.caseSize = self.boardSizeGlobal // self.numCase
        self.boardSizeBorder = self.boardSizeGlobal - self.caseSize


    def reset(self):
        self.activePlayer = 1
        self.currentScore = {1: 0, 2: 0}

    def getIndexFromPos(self, window, pos):
        board_origin = (window.size[0] // 2 - self.boardSizeGlobal // 2 + self.caseSize // 4, window.size[1] // 2 - self.boardSizeGlobal // 2.3 + self.caseSize // 4)
        x_rel = pos[0] - board_origin[0]
        y_rel = pos[1] - board_origin[1]
        if 0 <= x_rel < self.boardSizeGlobal and 0 <= y_rel < self.boardSizeGlobal:
            col = int(x_rel // self.caseSize)
            row = int(y_rel // self.caseSize)
            return (row, col)

    #not working
    def getPosFromIndex(self, row, col, window):
        board_origin = (window.size[0] // 2 - self.boardSizeGlobal // 2 + self.caseSize // 4, window.size[1] // 2 - self.boardSizeGlobal // 2.3 + self.caseSize // 4)
        x = board_origin[0] + col * self.caseSize
        y = board_origin[1] + row * self.caseSize
        return (x, y)

def init(window):
    Display = pg.display.set_mode(window.size)
    pg.display.set_caption("Gomoku")
    icon = pg.image.load("assets/image/icon_star_normal.png").convert_alpha()
    pg.display.set_icon(icon)
    return Display


def main():
    window = Window()
    game = Game()
    Display = init(window)

    window.loadAssets(game)                                                                                                                                                                                                            

    musicPlayer = classes.MusicPlayer("assets/sound/background_music.mp3")
    musicPlayer.play()
    soundEffects = classes.SoundEffects()
    # End TODO

    window.setButtons(game, soundEffects, musicPlayer)

    match game.displayedWindow:
        case 0:
            window.drawMainMenu(Display)
        case 1:
            window.drawGameScene(Display, game)
        case 2:
            window.drawSettingsMenu(Display)

    # Main game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False

            match game.displayedWindow:
                case 0:
                    window.playButton.update(event)
                    window.settingButton.update(event)
                case 1:
                    window.homeButton.update(event)
                    if event.type == MOUSEBUTTONDOWN:
                        game_move = game.getIndexFromPos(window, event.pos)
                        pos = game.getPosFromIndex(game_move[0], game_move[1], window)
                        pg.draw.circle(Display, (255, 0, 0), pos, 10)
                        print(pos)
                        pg.display.flip()
                        pg.time.delay(100)
                    # TODO: game logic
                    # check event in the game -> tie; win; switch player; invalid move; capture
                    # if AI mode, get AI move 
                case 2:
                    window.settingButton.update(event)
                    window.musicButton.update(event)
                    window.soundButton.update(event)
            window.exitButton.update(event)

        match game.displayedWindow:
            case 0:
                window.drawMainMenu(Display)
                game.reset()
            case 1:
                window.drawGameScene(Display, game)
            case 2:
                window.drawSettingsMenu(Display)

        pg.time.Clock().tick(window.fps)


if __name__ == "__main__":
    main()