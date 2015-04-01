﻿#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module permettant d'écouter les requêtes venant du serveur
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

from threading import Thread


class TcpListener(Thread):
    buffer = ""
    running = True
    dataSize = 0

    def __init__(self, soc, size):
        Thread.__init__(self)
        self.soc = soc
        self.dataSize = size

    def run(self):
        while (self.running):
            try:
                self.buffer += str(self.soc.recv(self.dataSize))
            except Exception as ex:
                return