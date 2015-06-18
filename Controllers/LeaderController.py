#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.3'

from struct import calcsize
import struct

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager
from Model.Leader import Leader
from Helper.StringHelper import StringHelper


class LeaderController(BaseController):
    def __init__(self, **kwargs):
        super(LeaderController, self).__init__(**kwargs)
        self.managerId = 4

    def getLeaders(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(2)  # Identifiant du controlleur
        req.addData("H", 5)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def getLeadersResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("!i50s255sii50s"):
                        response = struct.unpack('!i50s255sii50s', data)

                        leader = Leader()
                        leader.id = response[0]
                        leader.name = StringHelper().GetRealString(response[1])
                        leader.description = StringHelper().GetRealString(response[2])
                        leader.price = response[3]
                        leader.energy = response[4]
                        leader.effect = StringHelper().GetRealString(response[5])

                        self.app.gameManager.leaders.append(leader)

                        data = data[calcsize("!i50s255sii50s"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    def getUserLeaders(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(1)  # Identifiant du controlleur
        req.addData("H", 6)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback2)

    def getUserLeadersResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des leaders
                    while len(data) >= calcsize("!i"):
                        response = struct.unpack('!i', data)

                        self.app.gameManager.leaders.append(response[0])

                        data = data[calcsize("!i"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    # Variables contenant les fonction réponse
    callback1 = getLeadersResp
    callback2 = getUserLeadersResp
