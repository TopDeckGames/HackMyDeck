#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton

from GestionView.BaseElement import BaseElement

from Model.Deck import Deck as ModelDeck
from Model.Card import Card as ModelCard

from CustomWidget.Card import Card

Builder.load_file("GestionView/DecksElement.kv")


class DecksElement(BaseElement):
    deck = ObjectProperty()

    def __init__(self, **kwargs):
        super(DecksElement, self).__init__(**kwargs)

        self.bind(deck=self.deckChange)
        self.ids.deckCards.bind(minimum_height=self.ids.deckCards.setter('height'))
        self.ids.userCards.bind(minimum_height=self.ids.userCards.setter('height'))

    def deckChange(self, *args):
        if not isinstance(self.deck, ModelDeck):
            self.ids.cmdSave.opacity = 0
            raise Exception("Un objet de type deck est requis")

        self.ids.cmdSave.opacity = 1
        for value in self.deck.cards:
            item = DeckCard(value[0], value[1])
            self.ids.deckCards.add_widget(item)

        for value in self.sup.app.gameManager.user.cards:
            item = Card(value[0], size_hint=(0.3, 1))
            self.ids.userCards.add_widget(item)

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

    def save(self, *args):
        pass

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


class DeckCard(ToggleButton):
    card = ObjectProperty()
    number = NumericProperty()

    def __init__(self, card, number, **kwargs):
        if not isinstance(card, ModelCard):
            raise Exception("Un objet de typde card est requis")

        self.card = card
        self.number = number

        super(DeckCard, self).__init__(**kwargs)
