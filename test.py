#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget

from GameScreens.QGScreen import QGScreen

from Manager.GameManager import GameManager

class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

        self.gameManager = GameManager()

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