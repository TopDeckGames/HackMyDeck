#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.Card import Card


class TrapCard(Card):
    revealType = ""

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)