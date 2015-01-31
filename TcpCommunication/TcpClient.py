#!/usr/bin/python

"""
Module permettant la communication avec les serveurs C#
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import socket
import TcpRequest


class TcpClient:
    token = 0
    requests = ()

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

    def send(self, request):
        if isinstance(request, TcpRequest.TcpRequest):
            try:
                request.build(self.token)
            except Exception as ex:
                raise Exception("Erreur lors de la construction de la requete " + ex.message)

            try:
                self.soc.send(request.getRequest())
            except Exception as ex:
                raise Exception("Erreur lors de l'envoi de la requete " + ex.message)
        else:
            raise Exception("Un object de type TcpRequest est requis")

        self.requests += (request)
        self.token += 1