#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module permettant de traiter les messages du serveur
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import time

import struct
import hashlib
from threading import Thread
from TcpCommunication.TcpListener import TcpListener
from TcpCommunication.TcpClient import TcpClient


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
                # Récupèration de l'entête
                message = self.tcpListener.buffer[:self.message_length]
                self.tcpListener.buffer = self.tcpListener.buffer[self.message_length:]

                # On déchiffre les données
                header = struct.unpack('@IHH32s', message)

                token = header[0]
                size = header[1]
                state = header[2]
                checksum = header[3]

                #On attend qu'il y ai assez de données
                while len(self.tcpListener.buffer) < size:
                    time.sleep(0.01)

                #On récupère le message
                message = self.tcpListener.buffer[:size]
                #Si le message est erroné on passe
                if hashlib.md5(message).hexdigest() != checksum:
                    continue
                #Sinon on enlève le message du buffer pour le traiter
                nbPart = size / self.message_length
                if size % self.message_length > 0:
                    nbPart += 1
                self.tcpListener.buffer = self.tcpListener.buffer[self.message_length * nbPart:]

                #On récupère l'action à réaliser selon le token donné
                action = None
                for item in TcpClient.TOKEN_LIST:
                    if item[0] == token:
                        action = item

                #Si une action a étée trouvée on supprime l'élèment de la liste et on exécute l'action
                if action is not None:
                    TcpClient.TOKEN_LIST.remove(action)
                    action[1](state, message)