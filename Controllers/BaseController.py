#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget


class BaseController(Widget):
    app = ObjectProperty(None)
    managerId = NumericProperty(0)

    def __init__(self, **kwargs):
        super(BaseController, self).__init__(**kwargs)