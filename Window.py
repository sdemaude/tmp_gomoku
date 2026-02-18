import pygame as pg
from pygame.locals import *
from enum import Enum

class DisplayedWindow(Enum):
    MAIN_MENU = 1
    GAME_SCENE = 2
    SETTINGS = 3

import themes
from ThemeManager import ThemeManager
from Button import Button, ToggleButton
from ButtonClickHandler import ButtonClickHandler
from MusicPlayer import MusicPlayer
from PlayerIcon import PlayerIcon
from Position import Position, PositionUnit, PositionReference
from SoundEffects import SoundEffects
from assets import Assets

class Window:
    def __init__(self, game):
        self.game = game
        self.size = (1600, 900)
        self.fps = 30
        self.displayedWindow = DisplayedWindow.MAIN_MENU
        print(Assets.ICON)
        self.display = self.createDisplay("Gomoku", Assets.ICON.value)

        self.soundEffects = SoundEffects()
        self.musicPlayer = MusicPlayer()
        self.themeManager = ThemeManager(themes.THEMES, self, default="classic")

        self.player1Icon = PlayerIcon(self.themeManager, self.game, (self.size[0] // 2 - 300, 30), (100, 100), 1)
        self.player2Icon = PlayerIcon(self.themeManager, self.game, (self.size[0] // 2 + 200, 30), (100, 100), 2)

        self._setButtons()
        self.drawMainMenu()


    def createDisplay(self, name: str, iconPath: str):
        display = pg.display.set_mode(self.size)
        pg.display.set_caption(name)
        icon = pg.image.load(iconPath).convert_alpha()
        pg.display.set_icon(icon)
        return display


    def _setButtons(self):
        buttonClick = ButtonClickHandler(self.game, self)

        self.exitButton = Button(Assets.EXIT.value, Position(self, 96, 5, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.exit_button_click)
        self.settingButton = Button(Assets.SETTINGS.value, Position(self, 92, 5, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.setting_button_click)
        self.homeButton = Button(Assets.HOME.value, Position(self, 92, 5, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.home_button_click)

        self.musicButton = ToggleButton(Assets.MUSIC_ON.value, Assets.MUSIC_OFF.value, Position(self, 50, 50, PositionUnit.PERCENTAGE, PositionReference.CENTER), True, buttonClick.music_button_click)
        self.soundButton = ToggleButton(Assets.SOUND_ON.value, Assets.SOUND_OFF.value, Position(self, 50, 60, PositionUnit.PERCENTAGE, PositionReference.CENTER), True, buttonClick.sound_button_click)
        
        self.pvpButton = Button(Assets.PVP.value, Position(self, 33, 50, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.pvp_button_click)
        self.pveButton = Button(Assets.PVE.value, Position(self, 66, 50, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.pve_button_click)

        self.theme1Button = Button(Assets.THEME1.value, Position(self, 37, 67, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.theme1_button_click, False)
        self.theme2Button = Button(Assets.THEME2.value, Position(self, 67, 67, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.theme2_button_click, False)
        self.theme3Button = Button(Assets.THEME3.value, Position(self, 37, 80, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.theme3_button_click, False)
        self.theme4Button = Button(Assets.THEME4.value, Position(self, 67, 80, PositionUnit.PERCENTAGE, PositionReference.CENTER), buttonClick.theme4_button_click, False)

    def drawBackground(self):
        background = self.themeManager.getBackground()
        self.display.blit(pg.transform.scale(background, self.size), (0, 0))


    def drawSettingsMenu(self):
        self.drawBackground()

        font = pg.font.SysFont(self.themeManager.fontName, 100)
        title = font.render("Settings", True, (255, 255, 255))
        self.display.blit(title, (self.size[0] // 2 - title.get_width() // 2, 100))

        self.musicButton.draw(self.display)
        self.soundButton.draw(self.display)

        self.settingButton.draw(self.display)
        self.exitButton.draw(self.display)

        self.theme1Button.draw(self.display)
        self.theme2Button.draw(self.display)
        self.theme3Button.draw(self.display)
        self.theme4Button.draw(self.display)

        pg.display.flip()


    def drawBoard(self):
        color = self.themeManager.getBoardColor()
        circleRadius = 7
        lineWidth = 2

        # draw 19x19 grid
        for i in range(self.game.numCase):
            # vertical lines
            startPos = (self.game.boardBorderOrigin(self)[0] + i * self.game.caseSize - 1, self.game.boardBorderOrigin(self)[1] - 1)
            endPos = (self.game.boardBorderOrigin(self)[0] + i * self.game.caseSize - 1, self.game.boardBorderOrigin(self)[1] + self.game.boardBorderSize - 1)
            pg.draw.line(self.display, color, startPos, endPos, lineWidth)
            # horizontal lines
            startPos = (self.game.boardBorderOrigin(self)[0] - 1, self.game.boardBorderOrigin(self)[1] + i * self.game.caseSize - 1)
            endPos = (self.game.boardBorderOrigin(self)[0] + self.game.boardBorderSize - 1, self.game.boardBorderOrigin(self)[1] + i * self.game.caseSize - 1)
            pg.draw.line(self.display, color, startPos, endPos, lineWidth)
        
        # draw star points
        starPoints = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
    
        for point in starPoints:
            center = (self.game.boardBorderOrigin(self)[0] + point[0] * self.game.caseSize, self.game.boardBorderOrigin(self)[1] + point[1] * self.game.caseSize)
            pg.draw.circle(self.display, color, center, circleRadius)
        
        # draw pieces
        for row in range(self.game.numCase):
            for col in range(self.game.numCase):
                if self.game.boardState[row][col] != 0:
                    # TODO: replace with custom piece images from theme manager
                    pos = self.game.getPosFromIndex(row, col, self)
                    color = (0, 0, 0) if self.game.boardState[row][col] == 1 else (255, 255, 255)
                    pg.draw.circle(self.display, color, pos, self.game.caseSize // 2 - 2)


    def drawGameScene(self):
        self.drawBackground()
        self.drawBoard()

        self.exitButton.draw(self.display)
        self.homeButton.draw(self.display)

        self.player1Icon.draw(self.display)
        self.player2Icon.draw(self.display)

        # print scores
        font = pg.font.SysFont(self.themeManager.fontName, 90)
        score = font.render(f"{self.game.currentScore[1]} | {self.game.currentScore[2]}", True, (255, 255, 255))
        self.display.blit(score, (self.size[0] // 2 - score.get_width() // 2, 30))

        pg.display.flip()


    def drawMainMenu(self):
        self.drawBackground()

        font = pg.font.SysFont(self.themeManager.fontName, 90)
        title = font.render("Gomoku", True, (255, 255, 255))
        self.display.blit(title, (self.size[0] // 2 - title.get_width() // 2, 100))
        font = pg.font.SysFont(self.themeManager.fontName, 50)
        selectModeText = font.render("Select Game Mode:", True, (255, 255, 255))
        self.display.blit(selectModeText, (self.size[0] // 2 - selectModeText.get_width() // 2, 300))

        self.pvpButton.draw(self.display)
        self.pveButton.draw(self.display)

        self.exitButton.draw(self.display)
        #self.playButton.draw(self.display)
        self.settingButton.draw(self.display)

        pg.display.flip()
