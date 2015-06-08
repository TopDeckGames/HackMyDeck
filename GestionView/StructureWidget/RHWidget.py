#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import NumericProperty

from GestionView.StructureWidget.BaseWidget import BaseWidget

from CustomWidget.Leader import Leader

Builder.load_file("GestionView/StructureWidget/RHWidget.kv")


class RHWidget(BaseWidget):
    nbItems = 2
    currentPage = NumericProperty(0)
    nbPages = 1

    def __init__(self, **kwargs):
        super(RHWidget, self).__init__(**kwargs)

        self.nbPages = len(self.sup.app.gameManager.leaders) / self.nbItems + (
        len(self.sup.app.gameManager.leaders) / self.nbItems > 0)

        self.bind(currentPage=self.changePage)
        self.currentPage = 1

    def changePage(self, *args):
        self.currentPage = min(self.currentPage, self.nbPages)
        self.currentPage = max(self.currentPage, 1)

        self.ids.cmdFirst.opacity = int(self.currentPage > 1)
        self.ids.cmdPrev.opacity = int(self.currentPage > 1)
        self.ids.cmdLast.opacity = int(self.currentPage < self.nbPages)
        self.ids.cmdNext.opacity = int(self.currentPage < self.nbPages)

        self.ids.leader1.clear_widgets()
        self.ids.leader2.clear_widgets()

        if self.currentPage * 2 - 2 < len(self.sup.app.gameManager.leaders):
            self.ids.leader1.add_widget(
                Leader(self.sup.app.gameManager.leaders[self.currentPage * 2 - 2], size_hint=(1, 1)))

        if self.currentPage * 2 - 1 < len(self.sup.app.gameManager.leaders):
            self.ids.leader2.add_widget(
                Leader(self.sup.app.gameManager.leaders[self.currentPage * 2 - 1], size_hint=(1, 1)))
