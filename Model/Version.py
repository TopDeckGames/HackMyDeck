#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty

from Model.SuperModel import SuperModel


class Version(SuperModel):
    NAME_LENGTH = 50
    DESCRIPTION_LENGTH = 150

    id = NumericProperty(0)
    name = StringProperty()
    description = StringProperty()
    created = NumericProperty()
    deployed = NumericProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)