#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, DictProperty

from Model.SuperModel import SuperModel


class Deck(SuperModel):
    NAME_LENGTH = 50
    COLOR_LENGTH = 50

    id = NumericProperty(0)
    name = StringProperty()
    color = StringProperty()
    cards = DictProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)