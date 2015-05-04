#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, BooleanProperty

from Model.SuperModel import SuperModel

class Card(SuperModel):
    TITLE_LENGTH = 50
    DESCRIPTION_LENGTH = 50

    id = NumericProperty(0)
    title = StringProperty()
    description = StringProperty()
    costInGame = NumericProperty(0)
    costInStore = NumericProperty(0)
    isBuyable = BooleanProperty(False)
    type = StringProperty()
    rarity = NumericProperty(0)

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)