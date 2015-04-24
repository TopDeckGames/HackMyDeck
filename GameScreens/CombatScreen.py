#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module servant de plateau de jeu
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder

from GameScreen import GameScreen
from CustomWidget.CardLayout import CardLayout
from CustomWidget.CardContainer import CardContainer
from Model.Card import Card

Builder.load_file("GameScreens/CombatScreen.kv")


class CombatScreen(GameScreen):
    """Widget principal de l'ecran, herite de la classe mere des ecrans"""

    def __init__(self, **kwargs):
        super(CombatScreen, self).__init__(**kwargs)

        emptyCard = Card()
        emptyCard.id = 0
        emptyCard.title = "empty"
        self.ids.deckP2.addCard(emptyCard)