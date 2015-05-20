#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget

from kivy.properties import BooleanProperty


class GameManager(Widget):
    user = None
    decks = []
    loading = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(GameManager, self).__init__(**kwargs)
