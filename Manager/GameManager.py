#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget

from kivy.properties import BooleanProperty, ListProperty, ObjectProperty


class GameManager(Widget):
    user = ObjectProperty()
    decks = ListProperty([])

    cards = ListProperty([])
    structures = ListProperty([])
    leaders = ListProperty([])

    loading = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(GameManager, self).__init__(**kwargs)
