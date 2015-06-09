#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module d'affichage et d'interraction d'un leader
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder

from Model.Leader import Leader as ModelLeader

Builder.load_file("CustomWidget/Leader.kv")


class Leader(Widget):
    def __init__(self, leader, **kwargs):
        if not isinstance(leader, ModelLeader):
            raise Exception("Un objet de type leader est requis")

        super(Leader, self).__init__(**kwargs)

        self.leader = leader

        # Binding des données
        self.ids.title.text = self.leader.name
        self.ids.cost.text = "Coût : " + str(self.leader.price)
        self.ids.picture.source = "Images/Leaders/" + str(self.leader.id) + ".jpg"
        self.ids.description.text = self.leader.description
