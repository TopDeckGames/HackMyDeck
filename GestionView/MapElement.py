#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder

from GestionView.BaseElement import BaseElement

Builder.load_file("GestionView/MapElement.kv")


class MapElement(BaseElement):
    def __init__(self, **kwargs):
        super(MapElement, self).__init__(**kwargs)