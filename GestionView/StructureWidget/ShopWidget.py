#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.popup import Popup

from GestionView.StructureWidget.BaseWidget import BaseWidget

from CustomWidget.Card import Card
from CustomWidget.DynImage import DynImage

from Model.Card import Card as ModelCard

Builder.load_file("GestionView/StructureWidget/ShopWidget.kv")


class ShopWidget(BaseWidget):
    cards = []
    nbItems = 6
    currentPage = NumericProperty(0)
    nbPages = 1

    def __init__(self, **kwargs):
        super(ShopWidget, self).__init__(**kwargs)

        self.cards = []

        for item in self.sup.app.gameManager.cards:
            if item.isBuyable == True:
                self.cards.append(item)

        self.nbPages = len(self.cards) / self.nbItems + int(len(self.cards) % self.nbItems > 0)

        self.bind(currentPage=self.changePage)
        self.currentPage = 1

    def changePage(self, *args):
        self.unbind(currentPage=self.changePage)

        self.currentPage = min(self.currentPage, self.nbPages)
        self.currentPage = max(self.currentPage, 1)

        self.ids.cmdFirst.opacity = int(self.currentPage > 1)
        self.ids.cmdPrev.opacity = int(self.currentPage > 1)
        self.ids.cmdLast.opacity = int(self.currentPage < self.nbPages)
        self.ids.cmdNext.opacity = int(self.currentPage < self.nbPages)

        id = self.currentPage * self.nbItems - 1
        for item in self.ids.cards.children:
            item.clear_widgets()

            if id < len(self.cards):
                card = Card(self.cards[id], size_hint=(None, None), pos_hint={"center_x": 0.5, "center_y": 0.5})
                card.visible = True
                img = DynImage(size=card.size, opacity=0)
                img.bind(on_release=lambda x: self.popupCard(card.card))
                card.add_widget(img)
                item.add_widget(card)
            id -= 1

        self.bind(currentPage=self.changePage)

    def popupCard(self, card):
        popup = ShopPopup(card)
        popup.open()


class ShopPopup(Popup):
    card = ObjectProperty()

    def __init__(self, card, **kwargs):
        if not isinstance(card, ModelCard):
            raise Exception("Un objet de type card est requis")

        self.card = card
        self.auto_dismiss = False

        super(ShopPopup, self).__init__(**kwargs)

        cardView = Card(self.card, pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=(0.75, 1))
        cardView.visible = True
        self.ids.cardView.add_widget(cardView)

    def buy(self, *args):
        # Todo achat de la carte

        self.dismiss()
