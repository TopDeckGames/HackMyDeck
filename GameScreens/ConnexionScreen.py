#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module servant d'ecran de connexion
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image

from TcpCommunication.Manager import Manager

from GameScreen import GameScreen

from Controllers.UserController import UserController

Builder.load_file("GameScreens/ConnexionScreen.kv")


class ConnexionScreen(GameScreen):
    """Widget principal de l'ecran, herite de la classe mere des ecrans"""

    def __init__(self, **kwargs):
        super(ConnexionScreen, self).__init__(**kwargs)

        # A l'arrivée sur l'écran de connexion on se connecte au serveur de login
        try:
            self.app.tcpManager.close()
            self.app.tcpManager.connect(Manager.SERVEUR_LOGIN)
        except Exception as ex:
            self.showError(ex)

    def connexion(self, username, password):
        """Methode de connexion de l'utilisateur

        Arguments:
            username -- Identifiant de l'utilisateur
            password -- Mot de passe de l'utilisateur"""

        self.popup = ConnexionPopup(content=Image(source="Images/loader.gif"), title="Connexion", auto_dismiss=False)
        self.popup.open()

        try:
            userController = UserController(app=self.app)
            userController.connexion(username.text, password.text)
        except Exception as ex:
            self.popup.dismiss()
            self.popup = ConnexionPopup(content=Label(text="Connexion impossible"), title="Avertissement")
            print ex.message
            self.popup.open()

    def inscription(self):
        self.popup = RegisterPopup(title="Inscription", auto_dismiss=False)
        self.popup.ids.action.bind(on_press=self.register)
        self.popup.open()

    def register(self, object):
        if self.popup.ids.username.text.strip() == "":
            pass
        elif self.popup.ids.password.text.strip() == "":
            pass
        elif self.popup.ids.password2.text.strip() == "":
            pass
        elif self.popup.ids.email.text.strip() == "":
            pass
        elif self.popup.ids.password.text.strip() != self.popup.ids.password2.text.strip():
            pass
        else:
            login = self.popup.ids.username.text
            password = self.popup.ids.password.text
            email = self.popup.ids.email.text

            self.popup.dismiss()
            self.popup = ConnexionPopup(content=Image(source="Images/loader.gif"), title="Inscription",
                                        auto_dismiss=False)
            self.popup.open()

            try:
                userController = UserController(app=self.app)
                userController.register(login, password, email)
            except Exception as ex:
                self.popup.dismiss()
                self.popup = ConnexionPopup(content=Label(text="Inscription impossible"), title="Avertissement")
                print ex.message
                self.popup.open()

    def displayMessage(self, message, type):
        self.popup.dismiss()
        self.popup = ConnexionPopup(content=Label(text=message), title=type)
        self.popup.open()


class ConnexionPopup(Popup):
    """Widget popup definit dans le fichier .kv"""
    pass


class RegisterPopup(Popup):
    """Widget popup definit dans le fichier .kv"""
    pass