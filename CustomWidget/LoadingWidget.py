#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.animation import Animation
from kivy.properties import BooleanProperty
from kivy.clock import Clock

Builder.load_file("CustomWidget/LoadingWidget.kv")


class LoadingWidget(Widget):
    visible = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(LoadingWidget, self).__init__(**kwargs)
        self.opacity = 0

        Clock.schedule_interval(self.blinkTitle, 0.1)

    def setVisible(self, obj, bool):
        self.visible = bool

        if bool:
            anim = Animation(opacity=1, duration=2)
        else:
            anim = Animation(opacity=0, duration=2)
        anim.start(self)

    def blinkTitle(self, *args):
        if self.visible:
            if self.ids.title.opacity >= 1:
                self.ids.title.blink = -1
            elif self.ids.title.opacity <= 0:
                self.ids.title.blink = 1

            self.ids.title.opacity += 0.05 * self.ids.title.blink
