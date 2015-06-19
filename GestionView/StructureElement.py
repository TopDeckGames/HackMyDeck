#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from GestionView.BaseElement import BaseElement

from StructureWidget.BaseWidget import BaseWidget
from StructureWidget.RHWidget import RHWidget
from StructureWidget.ShopWidget import ShopWidget

from Controllers.StructureController import StructureController

from Model.Structure import Structure

Builder.load_file("GestionView/StructureElement.kv")


class StructureElement(BaseElement):
    structure = ObjectProperty()
    userStructure = ObjectProperty()

    def __init__(self, structures, **kwargs):
        if not isinstance(structures[0], Structure) or not isinstance(structures[1], Structure):
            raise Exception("Un objet model de structure est requis")
        self.structure = structures[0]
        self.userStructure = structures[1]

        super(StructureElement, self).__init__(**kwargs)

        if self.structure.type == 3:
            widget = RHWidget
        elif self.structure.type == 2:
            widget = ShopWidget
        else:
            widget = BaseWidget

        widget = widget(sup=self.sup, structure=self.structure, userStructure=self.userStructure, size_hint=(1, 1),
                        pos_hint={"left": 0, "top": 0})
        self.changeWidget(widget)

    def changeWidget(self, widget):
        if not isinstance(widget, BaseWidget):
            raise Exception("Une objet héritant de BaseWidget est requis")

        self.ids.container.clear_widgets()
        self.ids.container.add_widget(widget)

    def leave(self, *args):
        self.sup.changeElement(self.sup.defaultElement())

    def levelUpPopup(self, *args):
        self.popup = Popup(title="Vérification", size=("400dp", "200dp"), size_hint=(None, None), auto_dismiss=False)
        layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        layout.add_widget(
            Label(text="Voulez-vous améliorer ce batiment ?\n Cela vous coutera " + str(self.priceCalc()) + " crédits",
                  size_hint=(1, 0.7)))
        layout2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        button1 = Button(text="Oui")
        button2 = Button(text="Non")
        button1.bind(on_release=self.levelUp)
        button2.bind(on_release=self.popup.dismiss)
        layout2.add_widget(button1)
        layout2.add_widget(button2)
        layout.add_widget(layout2)
        self.popup.content = layout
        self.popup.open()

    def levelUp(self, *args):
        structureCtrl = StructureController(app=self.sup.app)
        if self.sup.app.gameManager.user.credits >= self.priceCalc():
            structureCtrl.levelUp(self.structure.id)
            self.popup.dismiss()

    def priceCalc(self):
        return 50 * self.userStructure.level
