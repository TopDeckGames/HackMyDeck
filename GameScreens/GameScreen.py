#!/usr/bin/python

"""
Module definissant la classe mere de tous les ecrans du jeu
"""

__author__ =  'Emile Taverne'
__version__=  '0.1'

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty

Builder.load_file("GameScreens/GameScreen.kv")

class GameScreen(Widget):
	"""Classe mere de tous les ecran du jeu"""
	app = ObjectProperty(None)