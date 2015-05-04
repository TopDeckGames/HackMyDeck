#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import NumericProperty, BooleanProperty

from Model.SuperModel import SuperModel


class Effect(SuperModel):
    id = NumericProperty(0)
    energy = NumericProperty()
    damage = NumericProperty()
    isBlocker = BooleanProperty(False)
    isCharge = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)