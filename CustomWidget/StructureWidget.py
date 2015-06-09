#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module d'affichage d'une structure sur la map
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty, BooleanProperty

from Model.Structure import Structure

from CustomWidget.DynImage import DynImage

Builder.load_file("CustomWidget/StructureWidget.kv")

class StructureWidget(Widget):
    structure = ObjectProperty()
    click = BooleanProperty(False)

    def __init__(self, structure, **kwargs):
        self.structure = structure

        super(StructureWidget, self).__init__(**kwargs)

        if not isinstance(structure, Structure):
            raise Exception("Un objet de type structure est requis")

        self.ids.image.bind(on_release=self.onClick)

    def selectFrame(self):
        if self.structure.level > 10:
            self.ids.image._coreimage._texture = self.ids.image._coreimage.image.textures[2]
        elif self.structure.level > 5:
            self.ids.image._coreimage._texture = self.ids.image._coreimage.image.textures[1]
        else:
            self.ids.image._coreimage._texture = self.ids.image._coreimage.image.textures[0]

        self.ids.image._coreimage.dispatch('on_texture')
        self.ids.image.anim_delay = -1

    def onClick(self, *args):
        self.click = True
