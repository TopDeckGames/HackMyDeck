#!/usr/bin/pythonho
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty, ListProperty

from Model.SuperModel import SuperModel

class User(SuperModel):
    LOGIN_LENGTH = 50
    PASSWORD_LENGTH = 16
    EMAIL_LENGTH = 60
    FIRSTNAME_LENGTH = 75
    LASTNAME_LENGTH = 75

    id = NumericProperty(0)
    login = StringProperty()
    password = StringProperty()
    credits = NumericProperty(0)
    nbWin = NumericProperty(0)
    nbConnexion = NumericProperty(1)
    isAdmin = BooleanProperty()

    cards = ListProperty()
    decks = ListProperty([])
    quests = ListProperty()
    skillTrees = ListProperty()
    structures = ListProperty()
    leaders = ListProperty()
    games = ListProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)