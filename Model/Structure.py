#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty

from Model.SuperModel import SuperModel


class Structure(SuperModel):
    id = NumericProperty()
    name = StringProperty()
    description = StringProperty()
    level = NumericProperty(1)

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)