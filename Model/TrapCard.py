#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty

from Model.Card import Card

class TrapCard(Card):
    REVEALTYPE_LENGTH = 50

    revealType = StringProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)