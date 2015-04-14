#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.SuperModel import SuperModel


class User(SuperModel):
    LOGIN_LENGTH = 50
    PASSWORD_LENGTH = 32
    FIRSTNAME_LENGTH = 75
    LASTNAME_LENGTH = 75

    id = None
    login = ""
    password = ""

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)