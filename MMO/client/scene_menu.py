from pygame.constants import KEYDOWN, K_BACKSPACE, K_RETURN, K_MINUS, K_TAB, K_INSERT

__author__ = 'Adrian'

import pygame
import fondo, boton, director, config, cursor, scene_game, scene
import sys


class SceneMenu(scene.Scene):
    def __init__(self):
        scene.Scene.__init__(self)
        self.fondo = fondo.Fondo(config.BACK_SCENE_MENU)
        self.btn_start = boton.Boton(config.PATH_ICONS + "start.png", config.PATH_ICONS + "start_select.png", x=240,
                                     y=220)
        self.btn_exit = boton.Boton(config.PATH_ICONS + "salir.png", config.PATH_ICONS + "salir_select.png", x=280,
                                    y=330)
        self.btn_start_rect = self.btn_start.rect
        self.btn_exit_rect = self.btn_exit.rect
        self.cursor = cursor.Cursor()

        self.nickname_text_rect = None
        self.nickname_border_rect = None
        self.password_text_rect = None
        self.password_border_rect = None

        self.nickname = "a"
        self.password = "a"

        self.current_string = self.nickname

        self.band = False

        self.colors_rect = [config.COLOR_BLACK, config.COLOR_GREY]

    def on_update(self):
        self.cursor.update()

    def on_event(self, events):
        inkey = None

        for event in events:
            if event.type == KEYDOWN:
                inkey = event.key
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.cursor.colliderect(self.btn_start_rect):
                    scene_next = scene_game.SceneGame(self.nickname, self.password)
                    dir = director.SingletonDirector()
                    dir.change_scene(scene_next)
                    dir.loop
                    break
                if self.cursor.colliderect(self.btn_exit_rect):
                    sys.exit()
                    break
                if self.cursor.colliderect(self.nickname_text_rect):
                    self.current_string = self.nickname
                    self.band = False
                if self.cursor.colliderect(self.password_text_rect):
                    self.current_string = self.password
                    self.band = True

        if inkey is None:
            pass
        elif inkey == K_BACKSPACE:
            self.current_string = self.current_string[0:-1]
        elif inkey == K_RETURN:
            pass
        elif inkey == K_MINUS:
            self.current_string.append("_")
        elif inkey == K_TAB:
            self.current_string = self.password
            self.band = True
        elif inkey == K_INSERT:
            scene_next = scene_game.SceneGame(self.dir, self.nickname, self.password)
            self.dir.change_scene(scene_next)
            self.dir.loop
        elif inkey <= 127:
            char = chr(inkey)
            # self.nickname.append(char)
            self.current_string += char
            # self.current_string += charan

        if self.band:
            self.password = self.current_string
        else:
            self.nickname = self.current_string

    def on_draw(self, screen):
        self.fondo.draw(screen)
        self.btn_start.update(screen, self.cursor)
        self.btn_exit.update(screen, self.cursor)
        self.display_box(screen, self.nickname, self.password)

    def display_box(self, screen, nickname, passowrd):
        "Print a message in a box in the middle of the screen"
        fontobject = pygame.font.Font(None, 36)

        self.nickname_text_rect = pygame.draw.rect(screen, config.COLOR_BLACK, ((screen.get_width() / 4), 40, (screen.get_width() / 2), 40), 0)
        self.nickname_border_rect = pygame.draw.rect(screen, config.COLOR_WHITE, ((screen.get_width() / 4), 40, (screen.get_width() / 2), 40), 1)

        self.password_text_rect = pygame.draw.rect(screen, config.COLOR_BLACK, ((screen.get_width() / 4), 120, (screen.get_width() / 2), 40), 0)
        self.password_border_rect = pygame.draw.rect(screen, config.COLOR_WHITE, ((screen.get_width() / 4), 120, (screen.get_width() / 2), 40), 1)

        screen.blit(fontobject.render("Nickname:", 1, config.COLOR_BLACK),
                        ((screen.get_width() / 4), 10))

        screen.blit(fontobject.render("Password:", 1, config.COLOR_BLACK),
                        ((screen.get_width() / 4), 90))

        if len(nickname) != 0:
            screen.blit(fontobject.render(str(nickname), 1, config.COLOR_WHITE),
                        ((screen.get_width() / 4) + 2, 40 + 8))

        if len(passowrd) != 0:
            hide = "*" * len(passowrd)
            screen.blit(fontobject.render(hide, 1, config.COLOR_WHITE),
                        ((screen.get_width() / 4) + 2, 120 + 8))

        # pygame.display.flip()



