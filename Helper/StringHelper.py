#!/usr/bin/python
# -*- coding: utf-8 -*-

class StringHelper:
    SEPARATOR = '*'

    def CompleteString(self, str, size):
        while len(str) < size:
            str += self.SEPARATOR

        return str