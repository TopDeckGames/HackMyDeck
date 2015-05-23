#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget

from GameScreens.QGScreen import QGScreen

from Manager.GameManager import GameManager

from Model.Structure import Structure

class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

        structure = Structure()
        structure.pos["left"] = 34.94
        structure.pos["right"] = 62.29
        structure.pos["top"] = 42.04
        structure.pos["bottom"] = 60.46

        self.gameManager = GameManager()
        self.gameManager.structures.append(structure)

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