#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from GestionView.StructureWidget.BaseWidget import BaseWidget

from CustomWidget.Leader import Leader

from Model.Leader import Leader as ModelLeader
from Model.Structure import Structure as ModelStructure

Builder.load_file("GestionView/StructureWidget/RHWidget.kv")

class RHWidget(BaseWidget):
    nbItems = 2
    currentPage = NumericProperty(0)
    nbPages = 1
    leaders = []

    def __init__(self, **kwargs):
        super(RHWidget, self).__init__(**kwargs)

        self.getLeaders()

        self.bind(currentPage=self.changePage)
        self.currentPage = 1

    def changePage(self, *args):
        self.unbind(currentPage=self.changePage)
        self.getLeaders()

        self.currentPage = min(self.currentPage, self.nbPages)
        self.currentPage = max(self.currentPage, 1)

        self.ids.cmdFirst.opacity = int(self.currentPage > 1)
        self.ids.cmdPrev.opacity = int(self.currentPage > 1)
        self.ids.cmdLast.opacity = int(self.currentPage < self.nbPages)
        self.ids.cmdNext.opacity = int(self.currentPage < self.nbPages)

        self.ids.leader1.clear_widgets()
        self.ids.leader2.clear_widgets()

        if self.currentPage * 2 - 2 < len(self.leaders):
            leader1 = Leader(self.leaders[self.currentPage * 2 - 2], size_hint=(1, 1))
            leader1.ids.cmdBuy.bind(on_release=lambda x: self.buy(leader1.leader.id))
            self.ids.leader1.add_widget(leader1)

        if self.currentPage * 2 - 1 < len(self.leaders):
            leader2 = Leader(self.leaders[self.currentPage * 2 - 1], size_hint=(1, 1))
            leader2.ids.cmdBuy.bind(on_release=lambda x: self.buy(leader2.leader.id))
            self.ids.leader2.add_widget(leader2)

        self.bind(currentPage=self.changePage)

    def getLeaders(self):
        self.leaders = []

        for item in self.sup.app.gameManager.leaders:
            exist = False
            for item2 in self.sup.app.gameManager.user.leaders:
                if item.id == item2.id:
                    exist = True
                    break

            if not exist:
                self.leaders.append(item)

        self.nbPages = len(self.leaders) / self.nbItems + (len(self.leaders) / self.nbItems > 0)

    def buy(self, id):
        leader = None
        structure = None

        for item in self.leaders:
            if item.id == id:
                leader = item
                break

        if not isinstance(leader, ModelLeader):
            raise Exception("Un objet de type leader est requis")

        for item in self.sup.app.gameManager.user.leaders:
            if item.id == leader.id:
                popup = Popup(title="Attention", content=Label(text="Vous avez déjà engagé cette personne"),
                              size_hint=(0.3, 0.15))
                popup.open()
                return

        for item in self.sup.app.gameManager.user.structures:
            if item.id == 0:
                structure = item
                break

        if not isinstance(structure, ModelStructure):
            raise Exception("Un objet de type structure est requis")

        if structure.level <= len(self.sup.app.gameManager.user.leaders):
            popup = Popup(title="Attention", content=Label(
                text="Vous avez atteinds votre maximum de chefs d'équipe, \naméliorez le batiment pour en débloquer d'avantage"),
                          size_hint=(0.3, 0.15))
            popup.open()
            return

        if self.sup.app.gameManager.user.credits < leader.price:
            popup = Popup(title="Attention",
                          content=Label(text="Vous ne possèdez pas assez de crédits pour recruter cette personne"),
                          size_hint=(0.3, 0.15))
            popup.open()
            return

        # Todo : Achat de la carte auprès du serveur
        self.sup.app.gameManager.user.credits -= leader.price
        self.sup.app.gameManager.user.leaders.append(leader)

        self.changePage()
