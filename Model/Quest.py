#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from Model.SuperModel import SuperModel


class Quest(SuperModel):
    NAME_LENGTH = 50
    TYPE_LENGTH = 50
    DESCRIPTION_LENGTH = 150
    CONDITIONS_LENGTH = 150

    id = NumericProperty(0)
    name = StringProperty()
    type = ObjectProperty()
    description = StringProperty()
    level = NumericProperty()
    credits = NumericProperty()
    conditions = StringProperty()
    created = NumericProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)