#!/usr/bin/python

"""
Module permettant de construire une requete a envoyer au serveur
"""

__author__ = 'Emile Taverne'
__version__ = '0.1'

import struct
import hashlib

class TcpRequest:
    structString = ""
    structData = ()

    def __init__(self, dataSize):
        self.dataSize = dataSize

    def addData(self, struc, data):
        try:
            self.structString = struc + self.structString
            self.structData = data + self.structData
        except Exception as ex:
            raise ex

    def setManager(self, idManager):
        self.idManager = idManager

    def build(self, token):
        self.token = token

        #On construit la structure des donnees a partir des elements enregistres
        self.sData = struct.Struct("<" + self.structString)
        try:
            self.data = self.sData.pack(*self.structData)
        except Exception as ex:
            raise ex

        #On calcule un md5 des donnees pour en verifier l'integrite cote serveur
        self.checksum = hashlib.md5(self.data).hexdigest()

        #On construit la structure de l'entete
        sHeader = struct.Struct("<IHH32s")
        values = (self.token, self.sData.size, self.idManager, self.checksum)

        try:
            self.header = sHeader.pack(*values)
        except Exception as ex:
            raise ex

    def getRequest(self):
        values = self.header + self.data

        str = struct.Struct("<c")
        data = str.pack(("0"))

        while len(values) % self.dataSize != 0:
            values += data

        return values