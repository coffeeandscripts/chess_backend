#!/usr/bin/env python3

"""
Chess
board.py
desc: classes to define each piece on the board
vers: 0.0.1
"""

class Pawn:
    def __init__(self, res):
        self.user = res
        self.char = "P"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
        
class Castle:
    def __init__(self, res):
        self.user = res
        self.char = "H"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()

class Knight:
    def __init__(self, res):
        self.user = res
        self.char = "Y"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()

class Bishop:
    def __init__(self, res):
        self.user = res
        self.char = "B"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()

class Queen:
    def __init__(self, res):
        self.user = res
        self.char = "Q"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()

class King:
    def __init__(self, res):
        self.user = res
        self.char = "K"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
