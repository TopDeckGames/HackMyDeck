#!/usr/bin/pythonho
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty, ListProperty

from Model.SuperModel import SuperModel

class User(SuperModel):
    LOGIN_LENGTH = 50
    PASSWORD_LENGTH = 32
    FIRSTNAME_LENGTH = 75
    LASTNAME_LENGTH = 75
    PSEUDO_LENGTH = 50

    id = NumericProperty(0)
    login = StringProperty()
    password = StringProperty()
    pseudo = StringProperty()
    credit = NumericProperty(0)
    nbWin = NumericProperty(0)
    nbConnexion = NumericProperty(1)
    isAdmin = BooleanProperty()
    cards = DictProperty()
    quests = ListProperty()
    skillTrees = ListProperty()
    structures = ListProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)