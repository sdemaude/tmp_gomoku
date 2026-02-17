import pygame as pg
from pygame.locals import *

import themes
from ThemeManager import ThemeManager
from Button import Button, ToggleButton
from ButtonClickHandler import ButtonClickHandler
from MusicPlayer import MusicPlayer
from PlayerIcon import PlayerIcon
from Position import Position, PositionUnit, PositionReference


class Window:
    def __init__(self, game):
        self.game = game
        self.size = (1600, 900)
        self.iconSize = 50
        self.fps = 30
        self.fontName = "Arial"
        self.display = self.createDisplay("Gomoku", "assets/image/icon_star_normal.png")
        self.themeManager = ThemeManager(themes.THEMES, self, default="classic")
        self.player1Icon = PlayerIcon(self.themeManager, self.game, (self.size[0] // 2 - 300, 30), (100, 100), 1)
        self.player2Icon = PlayerIcon(self.themeManager, self.game, (self.size[0] // 2 + 200, 30), (100, 100), 2)


    def createDisplay(self, name, icon_path):
        display = pg.display.set_mode(self.size)
        pg.display.set_caption(name)
        icon = pg.image.load(icon_path).convert_alpha()
        pg.display.set_icon(icon)
        return display


    def setButtons(self, soundEffects, musicPlayer):
        buttonClick = ButtonClickHandler(self.game, self, soundEffects, musicPlayer)

        self.exitButton = Button("assets/image/icon_exit.png", Position(self, 96, 1, PositionUnit.PERCENTAGE), (self.iconSize, self.iconSize), buttonClick.exit_button_click)
        self.settingButton = Button("assets/image/icon_settings.png", Position(self, 90, 1, PositionUnit.PERCENTAGE), (self.iconSize, self.iconSize), buttonClick.setting_button_click)
        self.homeButton = Button("assets/image/icon_home.png", Position(self, 96, 1, PositionUnit.PERCENTAGE), (self.iconSize, self.iconSize), buttonClick.home_button_click)

        self.musicButton = ToggleButton("assets/image/icon_music_on.png", "assets/image/icon_music_off.png", Position(self, 50, 50, PositionUnit.PERCENTAGE), (self.iconSize, self.iconSize), True, buttonClick.music_button_click)
        self.soundButton = ToggleButton("assets/image/icon_sound_on.png", "assets/image/icon_sound_off.png", Position(self, 50, 60, PositionUnit.PERCENTAGE), (self.iconSize, self.iconSize), True, buttonClick.sound_button_click)
        
        self.pvpButton = Button("assets/image/button_pvp.png", Position(self, 50, 50, PositionUnit.PERCENTAGE), (150, 100), buttonClick.pvp_button_click)
        self.pveButton = Button("assets/image/button_pve.png", Position(self, 75, 50, PositionUnit.PERCENTAGE), (150, 100), buttonClick.pve_button_click)

        self.theme1Button = Button("assets/image/button_theme1.png", Position(self, 50, 65, PositionUnit.PERCENTAGE), (150, 100), buttonClick.theme1_button_click, False)
        self.theme2Button = Button("assets/image/button_theme2.png", Position(self, 75, 65, PositionUnit.PERCENTAGE), (150, 100), buttonClick.theme2_button_click, False)
        self.theme3Button = Button("assets/image/button_theme3.png", Position(self, 50, 80, PositionUnit.PERCENTAGE), (150, 100), buttonClick.theme3_button_click, False)
        self.theme4Button = Button("assets/image/button_theme4.png", Position(self, 75, 80, PositionUnit.PERCENTAGE), (150, 100), buttonClick.theme4_button_click, False)    

        #self.playButton = Button("assets/image/button_play.png", (self.size[0] // 2 - 100, self.size[1] // 2 - 50), (100, 100), buttonClick.play_button_click)


    def drawBackground(self):
        background = self.themeManager.getBackground()
        self.display.blit(pg.transform.scale(background, self.size), (0, 0))


    def drawSettingsMenu(self):
        self.drawBackground()

        font = pg.font.SysFont(self.fontName, 100)
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
        # draw 19x19 grid
        for i in range(self.game.numCase):
            # vertical lines
            start_pos = (self.game.boardBorderOrigin(self)[0] + i * self.game.caseSize - 1, self.game.boardBorderOrigin(self)[1] - 1)
            end_pos = (self.game.boardBorderOrigin(self)[0] + i * self.game.caseSize - 1, self.game.boardBorderOrigin(self)[1] + self.game.boardBorderSize - 1)
            pg.draw.line(self.display, color, start_pos, end_pos, 2)
            # horizontal lines
            start_pos = (self.game.boardBorderOrigin(self)[0] - 1, self.game.boardBorderOrigin(self)[1] + i * self.game.caseSize - 1)
            end_pos = (self.game.boardBorderOrigin(self)[0] + self.game.boardBorderSize - 1, self.game.boardBorderOrigin(self)[1] + i * self.game.caseSize - 1)
            pg.draw.line(self.display, color, start_pos, end_pos, 2)
        
        # draw star points
        star_points = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
        for point in star_points:
            center = (self.game.boardBorderOrigin(self)[0] + point[0] * self.game.caseSize, self.game.boardBorderOrigin(self)[1] + point[1] * self.game.caseSize)
            pg.draw.circle(self.display, color, center, 7) # TODO: replace magic number with CONSTANT
        
        # draw pieces
        for row in range(self.game.numCase):
            for col in range(self.game.numCase):
                if self.game.boardState[row][col] != 0:
                    pos = self.game.getPosFromIndex(row, col, self)
                    color = (0, 0, 0) if self.game.boardState[row][col] == 1 else (255, 255, 255)
                    pg.draw.circle(self.display, color, pos, self.game.caseSize // 2 - 2) # TODO: replace magic number with CONSTANT


    def drawGameScene(self):
        self.drawBackground()
        self.drawBoard()

        self.exitButton.draw(self.display)
        self.homeButton.draw(self.display)

        self.player1Icon.draw(self.display)
        self.player2Icon.draw(self.display)

        # print scores
        font = pg.font.SysFont(self.fontName, 90)
        score = font.render(f"{self.game.currentScore[1]} | {self.game.currentScore[2]}", True, (255, 255, 255))
        self.display.blit(score, (self.size[0] // 2 - score.get_width() // 2, 30))

        pg.display.flip()


    def drawMainMenu(self):
        self.drawBackground()

        # draw pvp and pve buttons
        self.pvpButton.draw(self.display)
        self.pveButton.draw(self.display)


        self.exitButton.draw(self.display)
        #self.playButton.draw(self.display)
        self.settingButton.draw(self.display)

        pg.display.flip()
