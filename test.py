#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget

from GameScreens.QGScreen import QGScreen

from Manager.GameManager import GameManager

from Model.Structure import Structure
from Model.Leader import Leader
from Model.User import User
from Model.Card import Card
from Model.Game import Game

class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

        structure = Structure(id=0, level=2)
        structure.pos["left"] = 34.94
        structure.pos["right"] = 62.29
        structure.pos["top"] = 42.04
        structure.pos["bottom"] = 60.46

        structure1 = Structure(id=1, level=1)
        structure1.pos["left"] = 5
        structure1.pos["right"] = 30
        structure1.pos["top"] = 42.04
        structure1.pos["bottom"] = 60.46

        card = Card(id=0, title="Test", description="Ceci est une carte de test", isBuyable=True)

        leader = Leader(id=0)
        leader.name = "Bill Gates"
        leader.price = 50
        leader.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa est, pellentesque at eros vel, vestibulum imperdiet quam. Nam ullamcorper fermentum augue, nec eleifend lorem pulvinar elementum."

        leader1 = Leader(id=1)
        leader1.name = "Linus Torvalds"
        leader1.price = 50
        leader1.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa est, pellentesque at eros vel, vestibulum imperdiet quam. Nam ullamcorper fermentum augue, nec eleifend lorem pulvinar elementum."

        leader2 = Leader(id=2)
        leader2.name = "Richard Stallman"
        leader2.price = 50
        leader2.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa est, pellentesque at eros vel, vestibulum imperdiet quam. Nam ullamcorper fermentum augue, nec eleifend lorem pulvinar elementum."

        game = Game(id=0, victory=True, opponent="Jean-Kevin", created=1433939136)

        game1 = Game(id=1, victory=False, opponent="Sasuke_du_16", created=1433939136)

        user = User(credits=150, login="DarkKikoo75")
        user.structures.append(structure)
        user.structures.append(structure1)
        user.cards.append((card, 3))

        for i in range(12):
            user.games.append(game)
            user.games.append(game1)

        self.gameManager = GameManager()
        self.gameManager.user = user
        self.gameManager.structures.append(structure)
        self.gameManager.structures.append(structure1)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)
        self.gameManager.cards.append(card)

        for i in range(2):
            self.gameManager.leaders.append(leader)
            self.gameManager.leaders.append(leader1)
            self.gameManager.leaders.append(leader2)
        self.gameManager.leaders.append(leader1)

        screen = QGScreen(app=self, opacity=0)
        # screen = CombatScreen(app=self, opacity=0)
        self.add_widget(screen)
        screen.show()

        # structure = Structure(id=0, name="Test", description="Ceci est un batiment de test")
        # element = StructureElement(structure)
        # screen.changeElement(element)

class MyApp(App):
    def build(self):
        from kivy.base import EventLoop

        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.root = TestWidget()


if __name__ == '__main__':
    MyApp().run()