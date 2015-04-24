#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module d'affichage d'un conteneur de cartes
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ListProperty

from CustomWidget.Card import Card as CardView
from Model.Card import Card as CardModel

Builder.load_file("CustomWidget/CardLayout.kv")


class CardLayout(Widget):
    cards = ListProperty()
    click = True

    def __init__(self, **kwargs):
        super(CardLayout, self).__init__(**kwargs)

    def addCard(self, card):
        if isinstance(card, CardView):
            self.cards.insert(0, card)
            self.ids.container.add_widget(card)
            card.pos = (0, 0)
        elif isinstance(card, CardModel):
            cardView = CardView(card)
            cardView.pos = (0, 0)
            self.ids.container.add_widget(cardView)
            self.cards.insert(0, cardView)
        else:
            raise Exception("Un objet de type card est requis")

    def getNext(self, cardModel):
        if len(self.cards) > 0:
            if not isinstance(cardModel, CardModel):
                raise Exception("Un objet de type card model est requis")

            card = self.cards[0]
            del self.cards[0]

            card.card = CardView(cardModel)
            card.visible = True

            return card

    def on_touch_down(self, touch):
        if self.click:
            self.click = False

            card = CardModel()
            card.title = "Carte de test"
            card.description = "Ceci est un test"

            cardView = self.getNext(card)
            if isinstance(cardView, CardView):
                from kivy.animation import Animation

                anim = Animation(pos=(-600, -750))
                anim.start(cardView)
                cardView.unlock()

    def on_touch_up(self, touch):
        self.click = True