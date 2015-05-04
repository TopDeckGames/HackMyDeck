#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import NumericProperty

from Model.SuperModel import SuperModel


class Action(SuperModel):
    id = NumericProperty(0)
    minRange = NumericProperty()
    maxRange = NumericProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)