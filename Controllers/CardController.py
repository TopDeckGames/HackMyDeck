#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.3'

from struct import calcsize
import struct

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager
from Model.Card import Card
from Helper.StringHelper import StringHelper


class CardController(BaseController):
    def __init__(self, **kwargs):
        super(CardController, self).__init__(**kwargs)
        self.managerId = 3

    def getCards(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(2)  # Identifiant du controlleur
        req.addData("H", 3)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def getCardsResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("=i50s255siii?"):
                        response = struct.unpack('=i50s255siii?', data[:calcsize("=i50s255siii?")])

                        card = Card()
                        card.id = response[0]
                        card.title = StringHelper().GetRealString(response[1])
                        card.description = StringHelper().GetRealString(response[2])
                        card.rarity = response[3]
                        card.costInGame = response[4]
                        card.costInStore = response[5]
                        card.isBuyable = response[6]

                        self.app.gameManager.cards.append(card)

                        data = data[calcsize("=i50s255siii?"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    def getUserCards(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(3)  # Identifiant du controlleur
        req.addData("H", 1)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback2)

    def getUserCardsResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("=ii"):
                        response = struct.unpack('=ii', data)

                        self.app.gameManager.user.cards[response[0]] = response[1]

                        data = data[calcsize("=ii"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    # Variables contenant les fonction réponse
    callback1 = getCardsResp
    callback2 = getUserCardsResp
