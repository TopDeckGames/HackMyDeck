#!/usr/bin/python
# -*- coding: utf-8 -*

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget


class SuperModel(Widget):
    def __init__(self, **kwargs):
        super(Widget, self).__init__(**kwargs)