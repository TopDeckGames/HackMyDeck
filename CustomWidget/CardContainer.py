#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from CustomWidget.CardLayout import CardLayout

from CustomWidget.Card import Card as CardView
from Model.Card import Card as CardModel


class CardContainer(CardLayout):
    def __init__(self, **kwargs):
        super(CardContainer, self).__init__(**kwargs)

    def addCard(self, card):
        if len(self.cards) == 0:
            if isinstance(card, CardView):
                self.cards.insert(0, card)
                self.ids.container.add_widget(card)
                card.pos = (0, 0)
            else:
                raise Exception("Un objet de type card est requis")
        else:
            raise Exception("Une carte est déjà présente dans cet emplacement")