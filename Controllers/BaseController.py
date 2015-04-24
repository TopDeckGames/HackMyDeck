#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.2'

import struct

from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget


class BaseController(Widget):
    app = ObjectProperty(None)
    managerId = NumericProperty(0)

    def __init__(self, **kwargs):
        super(BaseController, self).__init__(**kwargs)

    def verifyResponse(self, data):
        if len(data) == 4:
            response = struct.unpack('i', data)

            if response[0] == 1:
                return True

        return False