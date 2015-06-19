#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.3'

from struct import calcsize
import struct

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager
from Model.Deck import Deck


class DeckController(BaseController):
    def __init__(self, **kwargs):
        super(DeckController, self).__init__(**kwargs)
        self.managerId = 5

    def getDecks(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(3)  # Identifiant du controlleur
        req.addData("H", 2)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def getDecksResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("=iii"):
                        response = struct.unpack('=iii', data)

                        deck = Deck()
                        deck.id = response[0]
                        deck.leader = response[1]

                        data = data[calcsize("=iii"):]

                        for i in range(response[2]):
                            rep = struct.unpack('=ii', data)
                            deck.cards[rep[0]] = rep[1]
                            data = data[calcsize("=ii"):]

                        self.app.gameManager.user.decks.append(deck)

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    # Variables contenant les fonction réponse
    callback1 = getDecksResp
