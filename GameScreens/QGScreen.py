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

from GameScreen import GameScreen

from GestionView.BaseElement import BaseElement
from GestionView.MapElement import MapElement

Builder.load_file("GameScreens/QGScreen.kv")


class QGScreen(GameScreen):
    """Widget de l'ecran"""

    credits = 150

    def __init__(self, **kwargs):
        super(QGScreen, self).__init__(**kwargs)

        # A l'arrivée sur l'écran de gestion on se connecte au serveur attribué
        # try:
        #    self.app.tcpManager.close()
        #    self.app.tcpManager.connect(Manager.SERVEUR_GESTION)
        #
        #    sData = struct.Struct("<i")
        #    data = sData.pack(*[GameManager.user.id])
        #    self.app.tcpManager.tcpClient.sendBytes(data)
        #except Exception as ex:
        #    self.showError(ex)

    def changeElement(self, element):
        if not isinstance(element, BaseElement):
            raise Exception("L'objet n'est pas un élément de vue valide")

        element.sup = self
        self.ids.container.clear_widgets()
        self.ids.container.add_widget(element)

    def defaultElement(self):
        return MapElement()