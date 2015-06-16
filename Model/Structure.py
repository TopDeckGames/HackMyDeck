#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, DictProperty

from Model.SuperModel import SuperModel

class Structure(SuperModel):
    NAME_LENGTH = 50
    TYPE_LENGTH = 50
    DESCRIPTION_LENGTH = 150

    id = NumericProperty(0)
    name = StringProperty()
    type = NumericProperty()
    description = StringProperty()
    level = NumericProperty(0)
    effectif = NumericProperty()
    pos = DictProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)