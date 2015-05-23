#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy

kivy.require('1.8.0')

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class DynImage(ButtonBehavior, Image):
    pass
