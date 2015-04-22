#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module d'affichage et d'interraction d'un carte
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.scatter import Scatter

Builder.load_file("CustomWidget/Card.kv")


class Card(Scatter):
    """Carte à jouer"""

    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

        self.do_rotation = False
        self.do_scale = False
        self.do_translation = True