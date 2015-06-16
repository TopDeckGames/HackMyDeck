#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget

from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, NumericProperty

from Controllers.UserController import UserController
from Controllers.StrucureController import StructureController

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

        self.nbLoading += 1
        userCtrl.getInfos()

        self.nbLoading += 1
        structureCtrl.getStructures()

    def isLoading(self, *args):
        self.loading = self.nbLoading > 0
