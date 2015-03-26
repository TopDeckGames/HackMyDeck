#!/usr/bin/python
# -*- coding: utf-8 -*-

from TcpCommunication.TcpClient import TcpClient
from TcpCommunication.TcpListener import TcpListener


class Manager:
    SERVEUR_LOGIN = ("127.0.0.1", 3000)
    MESSAGE_LENGTH = 40

    tcpClient = None
    tcpListener = None

    def connect(self, server):
        try:
            self.tcpClient = TcpClient(server[0], server[1])
            self.tcpListener = TcpListener(self.tcpClient.soc, self.MESSAGE_LENGTH)
            self.tcpListener.start()
        except Exception as ex:
            self.tcpClient = None
            self.tcpListener = None
            raise ex

    def close(self):
        if self.tcpClient != None:
            self.tcpClient.close()