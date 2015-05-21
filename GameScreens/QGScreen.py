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
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from GameScreen import GameScreen

from GestionView.BaseElement import BaseElement
from GestionView.MapElement import MapElement
from GestionView.DecksElement import DecksElement
from GestionView.StatsElement import StatsElement

from Controllers.GestionController import GestionController

from Manager.GameManager import GameManager

from TcpCommunication.Manager import Manager

import struct

Builder.load_file("GameScreens/QGScreen.kv")

class QGScreen(GameScreen):
    """Widget de l'ecran"""

    credits = 150
    actions = [("Accueil", MapElement), ("Mes decks", DecksElement), ("Mes statistiques", StatsElement)]
    currentAction = None

    def __init__(self, **kwargs):
        super(QGScreen, self).__init__(**kwargs)

        # A l'arrivée sur l'écran de gestion on se connecte au serveur attribué
        try:
            self.app.tcpManager.close()
            self.app.tcpManager.connect(Manager.SERVEUR_GESTION)

            sData = struct.Struct("<i")
            data = sData.pack(*[GameManager.user.id])
            self.app.tcpManager.tcpClient.sendBytes(data)
        except Exception as ex:
            self.showError(ex)

        self.currentAction = self.actions[0]
        self.changeElement(self.currentAction[1]())

        for item in self.actions:
            self.ids.spnActions.values.append(item[0])
        self.ids.spnActions.text = self.currentAction[0]
        self.ids.spnActions.bind(text=self.actionChange)

        self.ids.cmdAttack.bind(on_press=self.showAttackPopup)

    def changeElement(self, element):
        if not isinstance(element, BaseElement):
            raise Exception("L'objet n'est pas un élément de vue valide")

        element.sup = self
        self.ids.container.clear_widgets()
        self.ids.container.add_widget(element)

    def actionChange(self, *args):
        if self.ids.spnActions.text != self.currentAction[0]:
            for item in self.actions:
                if item[0] == self.ids.spnActions.text:
                    element = item[1]()
                    self.changeElement(element)
                    self.currentAction = item
                    return

    def showAttackPopup(self, *args):
        if self.ids.cmdAttack.text != "Annuler":
            self.deckSelect = Spinner(id="deckSelect", size_hint=(0.7, 1))

            for deck in self.app.gameManager.decks:
                self.deckSelect.values.append(deck.name)

            button = Button(text="Lancer", size_hint=(0.3, 1))
            button.bind(on_press=self.attack)

            content = StackLayout()
            content.add_widget(self.deckSelect)
            content.add_widget(button)

            self.popup = Popup(title='Combat', content=content, auto_dismiss=True, size_hint=(None, None),
                               size=("400dp", "100dp"))
            self.popup.open()
        else:
            self.ids.cmdAttack.text = "Attaquer"
            try:
                gestionController = GestionController(app=self.app)
                gestionController.stopAttack(self.app.gameManager.user)
            except Exception as ex:
                pass

    def attack(self, *args):
        if self.deckSelect.text.strip() != "":
            self.popup.dismiss()
            self.ids.cmdAttack.text = "Annuler"

            deck = None
            for element in self.app.gameManager.decks:
                if element.name == self.deckSelect.text.strip():
                    deck = element
                    break

            try:
                gestionController = GestionController(app=self.app)
                gestionController.attack(self.app.gameManager.user, deck)
            except Exception as ex:
                pass