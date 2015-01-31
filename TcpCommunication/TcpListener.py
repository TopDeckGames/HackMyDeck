#!/usr/bin/python

"""
Module permettant d'écouter les requêtes venant du serveur
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import socket
from threading import Thread

class TcpListener(Thread):
    def __init__(self, soc, size):
        Thread.__init__(self)
        self.soc = soc
        self.dataSize = size

    def run(self):
        while(True):
            try:
                data = self.soc.recv(self.dataSize)
            except Exception as ex:
                raise ex