#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty

from Model.SuperModel import SuperModel


class Leader(SuperModel):
    NAME_LENGTH = 50
    DESCRIPTION_LENGTH = 50

    id = NumericProperty(0)
    name = StringProperty()
    description = StringProperty()
    effect = StringProperty(0)
    energy = NumericProperty(0)
    price = NumericProperty(0)

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
