#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module de l'ecran concernant l'interface de gestion
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder

from GameScreen import GameScreen

Builder.load_file("GameScreens/QGScreen.kv")


class QGScreen(GameScreen):
    """Widget de l'ecran"""
    pass