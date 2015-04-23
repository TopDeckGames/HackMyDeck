#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.Card import Card


class TechnologyCard(Card):
    damage = 0

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)