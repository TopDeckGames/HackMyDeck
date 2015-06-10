#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty

from GestionView.BaseElement import BaseElement

from Model.Game import Game as GameModel

import datetime

Builder.load_file("GestionView/StatsElement.kv")


class StatsElement(BaseElement):
    def __init__(self, **kwargs):
        super(StatsElement, self).__init__(**kwargs)

        games = self.sup.app.gameManager.user.games

        id = 0
        for game in games:
            self.ids.container.add_widget(GameElement(game, sup=self.sup, size_hint=(1, 0.1)))
            id += 1
            if id >= 10:
                break


class GameElement(Widget):
    game = ObjectProperty()
    sup = ObjectProperty()
    color = [0, 0, 0, 1]

    def __init__(self, game, **kwargs):
        if not isinstance(game, GameModel):
            raise Exception("Un objet de type Game est requis")

        self.game = game
        self.date = datetime.datetime.fromtimestamp(game.created).strftime('%H:%M:%S %d/%m/%Y')

        if self.game.victory:
            self.color = [0, 1, 0, 1]
        else:
            self.color = [1, 0, 0, 1]

        super(GameElement, self).__init__(**kwargs)
