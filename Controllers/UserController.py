#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Emile Taverne'
__version__ = '0.1'

import hashlib

from Controllers.BaseController import BaseController
from TcpCommunication.TcpRequest import TcpRequest


class UserController(BaseController):
    def __init__(self, **kwargs):
        super(UserController, self).__init__(**kwargs)
        self.managerId = 1

    def connexion(self, login, password):
        if login.strip() == "" or password.strip() == "":
            raise Exception("Login ou mot de passe non valide")

        m = hashlib.md5()
        m.update(password)
        hash_password = m.digest()

        req = TcpRequest(40)
        req.setManager(self.managerId)
        req.addData("H", 1)
        req.addData(str(len(login)) + "s", login)
        req.addData(str(len(hash_password)) + "s", hash_password)

        self.app.tcpClient.send(req)