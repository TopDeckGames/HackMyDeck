#!/usr/bin/python
# -*- coding: utf-8 -*-

class StringHelper:
    SEPARATOR = '*'

    def CompleteString(self, str, size):
        while len(str) < size:
            str += self.SEPARATOR

        return str

    def GetRealString(self, str):
        return str.split(self.SEPARATOR)[0]
