#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import NumericProperty

from Model.Card import Card

class TechnologyCard(Card):
    damage = NumericProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)