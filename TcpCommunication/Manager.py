#!/usr/bin/python
# -*- coding: utf-8 -*-

from TcpCommunication.TcpClient import TcpClient
from TcpCommunication.TcpListener import TcpListener
from TcpCommunication.RequestHandler import RequestHandler


class Manager:
    SERVEUR_LOGIN = ("", 0)
    MESSAGE_LENGTH = 40
    SERVEUR_GESTION = None

    tcpClient = None
    tcpListener = None
    requestHandler = None

    def connect(self, server):
        try:
            self.tcpClient = TcpClient(server[0], server[1])
            self.tcpListener = TcpListener(self.tcpClient.soc, self.MESSAGE_LENGTH)
            self.requestHandler = RequestHandler(self.tcpListener, self.MESSAGE_LENGTH)
            self.tcpListener.daemon = True
            self.requestHandler.daemon = True
            self.tcpListener.start()
            self.requestHandler.start()
        except Exception as ex:
            self.tcpClient = None
            self.tcpListener = None
            raise ex

    def close(self):
        if self.tcpClient != None:
            self.tcpClient.close()
        if self.tcpListener != None:
            self.tcpListener.running = False
        if self.requestHandler != None:
            self.requestHandler.running = False