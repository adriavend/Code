#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame

import config, scene_menu


class SingletonDirector(object):

    """ Implementacion de un Singleton """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonDirector, cls).__new__(cls)
        return cls.instance

    """Representa el objeto Principal del Juego.
	
	El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.
 
    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption(config.NAME)
        self.clock = pygame.time.Clock()
        self.vx = 0
        self.vy = 0
        self.scene = scene_menu.SceneMenu()

    def loop(self):
        "Pone en Funcionamiento el Juego"
        while not config.QUIT_FLAG:
            self.time = self.clock.tick(20)

            #Eventos de Entrada
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.quit_flag = True

            # Detecta Eventos
            self.scene.on_event(events)

            # Actualiza la Escena
            self.scene.on_update()

            # Dibuja la Pantalla
            self.scene.on_draw(self.screen)

            # pygame.display.update()
            pygame.display.flip() #Actualizar la superficie de visualización por completo sobre la pantalla.

        # time.sleep(3)
        pygame.quit()

    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
