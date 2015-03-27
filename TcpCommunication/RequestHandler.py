#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module permettant de traiter les messages du serveur
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

from threading import Thread

from TcpCommunication.TcpListener import TcpListener


class RequestHandler(Thread):
    tcpListener = None
    message_length = 0
    running = True

    def __init__(self, tcpListener, message_length):
        Thread.__init__(self)
        if type(tcpListener) is TcpListener:
            self.tcpListener = tcpListener
        else:
            raise Exception("Variable incorrecte")
        self.message_length = message_length

    def run(self):
        while (self.running):
            if len(self.tcpListener.buffer) >= self.message_length:
                message = self.tcpListener.buffer[:self.message_length]