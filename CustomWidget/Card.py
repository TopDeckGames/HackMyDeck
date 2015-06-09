#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module d'affichage et d'interraction d'un carte
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.scatter import Scatter
from kivy.properties import ObjectProperty, BooleanProperty

from Model.Card import Card as ModelCard

Builder.load_file("CustomWidget/Card.kv")


class Card(Scatter):
    """Carte à jouer"""

    card = ObjectProperty()
    visible = BooleanProperty(False)

    def __init__(self, card, **kwargs):
        if not isinstance(card, ModelCard):
            raise Exception("Un objet de type card est requis")

        super(Card, self).__init__(**kwargs)

        self.card = card

        # Binding des données
        self.ids.title.text = self.card.title
        self.ids.cost.text = str(self.card.costInGame)
        self.ids.picture.source = "Images/Cards/" + str(self.card.id) + ".jpg"
        #self.ids.type.text
        self.ids.description.text = self.card.description
        #self.ids.effects.text =

        if self.card.rarity == 0:
            self.ids.title.color = [0.36, 0.55, 0.68, 1]
        elif self.card.rarity == 1:
            self.ids.title.color = [0.02, 0.58, 0.45, 1]
        elif self.card.rarity == 2:
            self.ids.title.color = [0.56, 0.27, 0.68, 1]
        elif self.card.rarity == 3:
            self.ids.title.color = [0.96, 0.67, 0.21, 1]

        #Configuration du scatter
        self.do_rotation = False
        self.do_scale = False
        self.do_translation = False

        self.show()
        self.bind(visible=self.show)

    def lock(self):
        self.do_translation = False

    def unlock(self):
        self.do_translation = True

    def show(self, *args):
        if self.visible:
            self.ids.background.source = "Images/Cards/front.jpg"
            for element in self.ids.container.children:
                element.opacity = 1
        else:
            self.ids.background.source = "Images/Cards/back.jpg"
            for element in self.ids.container.children:
                element.opacity = 0