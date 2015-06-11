#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from GestionView.BaseElement import BaseElement

from Model.Deck import Deck as ModelDeck

Builder.load_file("GestionView/DecksElement.kv")


class DecksElement(BaseElement):
    deck = ObjectProperty()

    def __init__(self, **kwargs):
        super(DecksElement, self).__init__(**kwargs)

        self.bind(deck=self.deckChange)

    def deckChange(self, *args):
        if not isinstance(self.deck, ModelDeck):
            self.ids.cmdSave.opacity = 0
            raise Exception("Un objet de type deck est requis")

        self.ids.cmdSave.opacity = 1

    def showLoadingPopup(self, *args):
        popup = LoadPopup(sup=self.sup)
        popup.bind(on_dismiss=self.load)
        popup.open()

    def showCreatePopup(self, *args):
        popup = CreatePopup(sup=self.sup)
        popup.open()

    def load(self, popup):
        if popup.deck:
            self.deck = popup.deck
            self.canvas.ask_update()


class LoadPopup(Popup):
    sup = ObjectProperty()
    items = []
    deck = ObjectProperty()

    def __init__(self, **kwargs):
        super(LoadPopup, self).__init__(**kwargs)

        self.items = []

        for deck in self.sup.app.gameManager.user.decks:
            self.items.append(deck.name)

        self.ids.decksList.values = self.items
        self.auto_dismiss = True

    def load(self, *args):
        if len(self.ids.decksList.text.strip()) == 0:
            return

        for deck in self.sup.app.gameManager.user.decks:
            if deck.name == self.ids.decksList.text.strip():
                self.deck = deck
                break

        self.dismiss()


class CreatePopup(Popup):
    sup = ObjectProperty()
    items = []

    def __init__(self, **kwargs):
        super(CreatePopup, self).__init__(**kwargs)

        self.items = []

        for leader in self.sup.app.gameManager.user.leaders:
            self.items.append(leader.name)

        self.ids.leadersList.values = self.items
        self.auto_dismiss = True

    def create(self, *args):
        if len(self.ids.name.text.strip()) == 0 or len(self.ids.leadersList.text.strip()) == 0:
            return

        for item in self.sup.app.gameManager.user.leaders:
            if item.name == self.ids.leadersList.text.strip():
                leader = item

        # Todo action de création de deck
        deck = ModelDeck(name=self.ids.name.text.strip(), leader=leader)
        self.sup.app.gameManager.user.decks.append(deck)

        self.dismiss()
