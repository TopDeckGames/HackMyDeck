#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty

Builder.load_file("GestionView/BaseElement.kv")


class BaseElement(Widget):
    sup = ObjectProperty()

    def __init__(self, **kwargs):
        super(BaseElement, self).__init__(**kwargs)