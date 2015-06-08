#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty

Builder.load_file("GestionView/StructureWidget/BaseWidget.kv")


class BaseWidget(Widget):
    sup = ObjectProperty()

    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__(**kwargs)
