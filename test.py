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

class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

        structure = Structure(id=0, level=2)
        structure.pos["left"] = 34.94
        structure.pos["right"] = 62.29
        structure.pos["top"] = 42.04
        structure.pos["bottom"] = 60.46

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

        user = User(credits=150)
        user.structures.append(structure)

        self.gameManager = GameManager()
        self.gameManager.user = user
        self.gameManager.structures.append(structure)

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