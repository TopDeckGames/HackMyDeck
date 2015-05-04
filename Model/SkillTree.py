#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty

from Model.SuperModel import SuperModel


class Enhancement(SuperModel):
    LABEL_LENGTH = 50
    TYPE_LENGTH = 50

    id = NumericProperty(0)

    label = StringProperty()
    type = StringProperty()
    effectifs = NumericProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)