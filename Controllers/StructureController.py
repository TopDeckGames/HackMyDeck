#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.3'

from struct import calcsize
import struct

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager
from Model.Structure import Structure
from Helper.StringHelper import StringHelper


class StructureController(BaseController):
    def __init__(self, **kwargs):
        super(StructureController, self).__init__(**kwargs)
        self.managerId = 2

    def getStructures(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(2)  # Identifiant du controlleur
        req.addData("H", 4)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def getStructuresResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("=i50s255sidddd"):
                        response = struct.unpack('=i50s255sidddd', data[:calcsize("=i50s255sidddd")])

                        structure = Structure()
                        structure.id = response[0]
                        structure.name = StringHelper().GetRealString(response[1])
                        structure.description = StringHelper().GetRealString(response[2])
                        structure.type = response[3]
                        structure.pos["left"] = response[4]
                        structure.pos["right"] = response[4] + response[6]
                        structure.pos["bottom"] = response[5]
                        structure.pos["top"] = response[5] - response[7]

                        self.app.gameManager.structures.append(structure)

                        data = data[calcsize("=i50s255sidddd"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    def getUserStructures(self):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(1)  # Identifiant du controlleur
        req.addData("H", 1)  # Identifiant de l'action

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback2)

    def getUserStructuresResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    from Manager.GameManager import GameManager

                    # On récupère les informations des structures
                    while len(data) >= calcsize("=ii?i"):
                        response = struct.unpack('=ii?i', data[:calcsize("=ii?i")])

                        structure = Structure()
                        structure.id = response[0]
                        structure.level = response[1]
                        structure.locked = response[2]
                        structure.effectif = response[3]

                        self.app.gameManager.user.structures.append(structure)

                        data = data[calcsize("=ii?i"):]

                    self.app.gameManager.nbLoading -= 1

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)
            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    def levelUp(self, idStructure):
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(1)  # Identifiant du controlleur
        req.addData("H", 8)  # Identifiant de l'action

        req.addData("i", idStructure)

        # Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback3)

    def levelUpResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    response = struct.unpack('=i', data[:calcsize("=i")])

                    for item in self.app.gameManager.user.structures:
                        if item.id == response[0]:
                            self.app.gameManager.user.credits -= 50 * item.level
                            item.level += 1
                            break

                except Exception as ex:
                    raise Exception("Impossible de lire les données : " + ex.message)

            else:
                raise Exception("La récupèration des informations a échoué")
        else:
            raise Exception("La récupèration des informations a échoué")

    # Variables contenant les fonction réponse
    callback1 = getStructuresResp
    callback2 = getUserStructuresResp
    callback3 = levelUpResp
