#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module permettant la communication avec les serveurs C#
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import socket

import TcpRequest


class TcpClient:
    token = 0
    TOKEN_LIST = []

    def __init__(self, address, port):
        self.port = port
        self.address = address
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.soc.connect((self.address, self.port))
        except Exception as ex:
            raise ex

    def close(self):
        try:
            self.soc.close()
        except Exception as ex:
            raise ex

    def send(self, request, callback):
        # On teste le type de l'objet
        if isinstance(request, TcpRequest.TcpRequest):
            try:
                #On construit la requête
                request.build(self.token)
            except Exception as ex:
                raise Exception("Erreur lors de la construction de la requete " + ex.message)

            #Envoi
            try:
                self.soc.send(request.getRequest())
            except Exception as ex:
                raise Exception("Erreur lors de l'envoi de la requete " + ex.message)
        else:
            raise Exception("Un object de type TcpRequest est requis")

        #On enregistre le token et la fonction de retour dans la liste
        TcpClient.TOKEN_LIST.append((self.token, callback))
        self.token += 1

    def sendBytes(self, bytes):
        try:
            self.soc.send(bytes)
        except Exception as ex:
            raise Exception("Erreur lors de l'envoi de la requete " + ex.message)