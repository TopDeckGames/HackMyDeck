#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.Card import Card


class UnitCard(Card):
    energy = 0
    damage = 0
    nbAttack = 0

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)