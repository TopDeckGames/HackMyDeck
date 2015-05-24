#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder

from GestionView.BaseElement import BaseElement
from GestionView.StructureElement import StructureElement

from CustomWidget.StructureWidget import StructureWidget

Builder.load_file("GestionView/MapElement.kv")


class MapElement(BaseElement):
    structures = []

    def __init__(self, **kwargs):
        super(MapElement, self).__init__(**kwargs)

        for structure in self.sup.app.gameManager.structures:
            widget = StructureWidget(structure)
            self.structures.append(widget)
            widget.bind(click=self.goToStructure)
            self.add_widget(widget)

        self.bind(size=self.update)
        self.update()

    def update(self, *args):
        for widget in self.structures:
            widget.size = ((widget.structure.pos["right"] - widget.structure.pos["left"]) * self.width / 100,
                           (widget.structure.pos["bottom"] - widget.structure.pos["top"]) * self.height / 100)
            widget.pos = (
                widget.structure.pos["left"] * self.width / 100,
                (100 - widget.structure.pos["bottom"]) * self.height / 100)

    def goToStructure(self, obj, val):
        self.sup.changeElement(StructureElement, obj.structure)
