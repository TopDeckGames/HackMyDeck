#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import NumericProperty, DictProperty

from Model.Card import Card

class UnitCard(Card):
    energy = NumericProperty()
    damage = NumericProperty()
    nbAttack = NumericProperty()
    effects = DictProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)