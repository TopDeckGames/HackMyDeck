#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module de l'ecran concernant l'interface de gestion
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder

from TcpCommunication.Manager import Manager

from GameScreen import GameScreen

Builder.load_file("GameScreens/QGScreen.kv")


class QGScreen(GameScreen):
    """Widget de l'ecran"""

    def __init__(self, **kwargs):
        super(QGScreen, self).__init__(**kwargs)

        # A l'arrivée sur l'écran de gestion on se connecte au serveur attribué
        try:
            self.app.tcpManager.close()
            self.app.tcpManager.connect(Manager.SERVEUR_GESTION)
        except Exception as ex:
            self.showError(ex)