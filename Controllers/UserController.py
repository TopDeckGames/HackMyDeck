#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.3'

import hashlib
import struct
import socket

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest
from TcpCommunication.Manager import Manager
from Model.User import User
from Helper.StringHelper import StringHelper
from Manager.GameManager import GameManager


class UserController(BaseController):
    def __init__(self, **kwargs):
        super(UserController, self).__init__(**kwargs)
        self.managerId = 1

    def connexion(self, login, password):
        if login.strip() == "" or password.strip() == "":
            raise Exception("Login ou mot de passe non valide")

        # Cryptage du mot de passe
        m = hashlib.md5()
        m.update(password)
        hash_password = m.digest()

        # On complète les chaines de charactères pour qu'elles fassent la longueur maximale
        login = StringHelper().CompleteString(login, User.LOGIN_LENGTH)

        # Préparation de la requête
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(self.managerId)
        req.addData("H", 1)  #Identifiant de la méthode distante à appeler
        #Ajout des données
        req.addData(str(User.LOGIN_LENGTH) + "s", login)
        req.addData(str(User.PASSWORD_LENGTH) + "s", hash_password)

        #Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback1)

    def connexionResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            # On vérifie que la requête a bien étée un succés
            if self.verifyResponse(data[:4]):
                data = data[4:]

                try:
                    #On récupère les informations du joueur
                    response = struct.unpack('iH', data[:6])

                    GameManager.user = User()
                    GameManager.user.id = response[0]
                    flag = response[1]

                    # Si il y a un serveur de disponible on le récupère
                    if flag == 1:
                        data = data[6:]
                        response = struct.unpack('ii', data[:8])

                        server = response[0]
                        port = response[1]

                        #On enregistre le serveur de gestion à contacter
                        Manager.SERVEUR_GESTION = (socket.inet_ntoa(struct.pack('L', server)), port)
                        #Changement d'écran
                        self.app.gameScreen.popup.dismiss()
                        self.app.changeScreen("QGScreen")
                    else:
                        self.app.gameScreen.displayMessage("Aucun serveur disponible, veuillez retenter plus tard",
                                                           "Information")
                    return
                except Exception as ex:
                    print ex.message
                    return

            self.app.gameScreen.displayMessage("Identifiants incorrects", "Avertissement")

        else:
            self.app.gameScreen.displayMessage("Connexion impossible", "Avertissement")

    def register(self, login, password, firstname, lastname):
        if login.strip() == "" or password.strip() == "" or firstname.strip() == "" or lastname.strip() == "":
            raise Exception("Donnée manquante")  # Cryptage du mot de passe

        m = hashlib.md5()
        m.update(password)
        hash_password = m.digest()

        # On complète les chaines de charactères pour qu'elles fassent la longueur maximale
        login = StringHelper().CompleteString(login, User.LOGIN_LENGTH)
        firstname = StringHelper().CompleteString(firstname, User.FIRSTNAME_LENGTH)
        lastname = StringHelper().CompleteString(lastname, User.LASTNAME_LENGTH)

        # Préparation de la requête
        req = TcpRequest(Manager.MESSAGE_LENGTH)
        req.setManager(self.managerId)
        req.addData("H", 2)  #Identifiant de la méthode distante à appeler
        #Ajout des données
        req.addData(str(User.LOGIN_LENGTH) + "s", login)
        req.addData(str(User.PASSWORD_LENGTH) + "s", hash_password)
        req.addData(str(User.FIRSTNAME_LENGTH) + "s", firstname)
        req.addData(str(User.LASTNAME_LENGTH) + "s", login)

        #Envoi
        self.app.tcpManager.tcpClient.send(req, self.callback2)

    def registerResp(self, state, data):
        # On vérifie qu'il n'y a pas eu d'erreur technique
        if state == 1:
            #On vérifie que la requête a bien étée un succés
            if self.verifyResponse(data[:4]):
                self.app.gameScreen.displayMessage("Inscription réalisée", "Information")

            self.app.gameScreen.displayMessage("Inscription impossible", "Avertissement")
        else:
            self.app.gameScreen.displayMessage("Inscription impossible", "Avertissement")

    # Variables contenant les fonction réponse
    callback1 = connexionResp
    callback2 = registerResp