#!/usr/bin/pythonho
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.properties import StringProperty, NumericProperty

from Model.SuperModel import SuperModel


class User(SuperModel):
    LOGIN_LENGTH = 50
    PASSWORD_LENGTH = 32
    FIRSTNAME_LENGTH = 75
    LASTNAME_LENGTH = 75

    id = NumericProperty(0)
    login = StringProperty()
    password = StringProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)