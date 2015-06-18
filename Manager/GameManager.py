#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget

from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, NumericProperty

from Controllers.UserController import UserController
from Controllers.StructureController import StructureController
from Controllers.CardController import CardController
from Controllers.LeaderController import LeaderController
from Controllers.DeckController import DeckController

class GameManager(Widget):
    user = ObjectProperty()

    cards = ListProperty([])
    structures = ListProperty([])
    leaders = ListProperty([])
    skillTrees = ListProperty()

    loading = BooleanProperty(False)
    nbLoading = NumericProperty(0)

    def __init__(self, **kwargs):
        super(GameManager, self).__init__(**kwargs)

        self.bind(nbLoading=self.isLoading)

    def load(self, app):
        userCtrl = UserController(app=app)
        structureCtrl = StructureController(app=app)
        cardCtrl = CardController(app=app)
        leaderCtrl = LeaderController(app=app)
        deckCtrl = DeckController(app=app)

        self.nbLoading += 2
        userCtrl.getInfos()
        userCtrl.getHistory()

        self.nbLoading += 2
        structureCtrl.getStructures()
        structureCtrl.getUserStructures()

        self.nbLoading += 2
        cardCtrl.getCards()
        cardCtrl.getUserCards()

        self.nbLoading += 1
        leaderCtrl.getLeaders()

        self.nbLoading += 1
        deckCtrl.getDecks()

    def isLoading(self, *args):
        self.loading = self.nbLoading > 0
