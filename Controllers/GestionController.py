#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

from BaseController import BaseController

from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager


class GestionController(BaseController):
    def __init__(self, **kwargs):
        super(GestionController, self).__init__(**kwargs)
        self.managerId = 2

    def attack(self, user, deck):
        # Préparation de la requête
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(self.managerId)
        req.addData("H", 1)  # Identifiant de la méthode distante à appeler
        # Ajout des données
        req.addData("i", user.id)
        req.addData("i", deck.id)

        #Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def attackResp(self, state, data):
        pass

    def stopAttack(self, user):
        # Préparation de la requête
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(self.managerId)
        req.addData("H", 2)  # Identifiant de la méthode distante à appeler
        # Ajout des données
        req.addData("i", user.id)

        #Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback2)

    def stopAttackResp(self, state, data):
        pass

    # Variables contenant les fonction réponse
    callback1 = attackResp
    callback2 = stopAttackResp