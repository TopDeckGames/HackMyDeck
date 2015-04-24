#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget

from Model.Card import Card

from GameScreens.CombatScreen import CombatScreen


class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

        screen = CombatScreen(app=self, opacity=0)
        self.add_widget(screen)
        screen.show()


class MyApp(App):
    def build(self):
        from kivy.base import EventLoop

        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.root = TestWidget()


if __name__ == '__main__':
    MyApp().run()