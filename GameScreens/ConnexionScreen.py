#!/usr/bin/python

"""
Module servant d'ecran de connexion
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import kivy

kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image

from GameScreen import GameScreen

Builder.load_file("GameScreens/ConnexionScreen.kv")


class ConnexionScreen(GameScreen):
    """Widget principal de l'ecran, herite de la classe mere des ecrans"""

    def connexion(self, username, password):
        """Methode de connexion de l'utilisateur

        Arguments:
            username -- Identifiant de l'utilisateur
            password -- Mot de passe de l'utilisateur"""

        popup = ConnexionPopup(content=Image(source="Images/loader.gif"), title="Connexion", auto_dismiss=False)
        popup.open()

        if username.text == "test" and password.text == "test":
            popup.dismiss()
            self.app.changeScreen("QGScreen");
        else:
            password.text = ""
            popup.dismiss()
            popup = ConnexionPopup(content=Label(text="Identifiants incorrects"), title="Avertissement")
            popup.open()


    def inscription(self):
        pass


class ConnexionPopup(Popup):
    """Widget popup definit dans le fichier .kv"""
    pass