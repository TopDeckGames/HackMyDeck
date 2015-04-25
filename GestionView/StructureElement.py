#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import ObjectProperty

from GestionView.BaseElement import BaseElement

from StructureWidget.BaseWidget import BaseWidget

from Model.Structure import Structure

Builder.load_file("GestionView/StructureElement.kv")


class StructureElement(BaseElement):
    structure = ObjectProperty()

    def __init__(self, structure, **kwargs):
        if not isinstance(structure, Structure):
            raise Exception("Un objet model de structure est requis")
        self.structure = structure

        super(StructureElement, self).__init__(**kwargs)

        if self.structure.id == 1:
            pass
        else:
            widget = BaseWidget()

        self.changeWidget(widget)

    def changeWidget(self, widget):
        if not isinstance(widget, BaseWidget):
            raise Exception("Une objet héritant de BaseWidget est requis")

        self.ids.container.clear_widgets()
        self.ids.container.add_widget(widget)

    def leave(self, *args):
        self.sup.changeElement(self.sup.defaultElement())