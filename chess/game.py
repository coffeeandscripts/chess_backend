#!/usr/bin/env python3

"""
Chess
game.py
desc: classes to define a running game
vers: 0.0.1
"""

from datetime import datetime
from .board import Board

class Game:
    def __init__(self):
        self.start_time = datetime.now()
        self.last_updated = datetime.now()
        self.board = Board()

    def __str__(self):
        return ("Chess: game started at " + str(self.start_time))

    def print_help(self):
        print("Chess: backend")
        print("Pieces:")
        print("* lowercase letters are the opponent, you are the uppercase letters")
        print("P - pawn")
        print("H - castle")
        print("Y - knight")
        print("B - bishop")
        print("Q - queen")
        print("K - king")
