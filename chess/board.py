#!/usr/bin/env python3

"""
Chess
board.py
desc: classes to define the arrangement of the board
vers: 0.0.1
"""

from .piece import *
import sys

class Board:
    def __init__(self):
        self.board = [[" "]*8 for _ in range(8)]
        self.populate_board()

    def __str__(self):
        return self.print_top_line() + self.print_board() + self.print_bottom_line()

    def print_top_line(self):
        return ("     A   B   C   D   E   F   G   H\n   +-------------------------------+\n")

    def print_board(self):
        txt = ""
        c = 8
        for n in self.board:
            txt += " " + str(c) + " |"
            for m in n:
                txt += " " + str(m) + " |"
            txt += " " + str(c) + "\n"
            if c > 1:
                txt += "   |-------------------------------|\n"
            c -= 1
        return txt
                

    def print_bottom_line(self):
        return ("   +-------------------------------+\n     A   B   C   D   E   F   G   H")

    def populate_board(self):
        self.board[0][0] = Castle(False)
        self.board[0][1] = Knight(False)
        self.board[0][2] = Bishop(False)
        self.board[0][3] = Queen(False)
        self.board[0][4] = King(False)
        self.board[0][5] = Bishop(False)
        self.board[0][6] = Knight(False)
        self.board[0][7] = Castle(False)
        for n in range(0,8):
            self.board[1][n] = Pawn(False)
        for n in range(0,8):
            self.board[6][n] = Pawn(True)
        self.board[7][0] = Castle(True)
        self.board[7][1] = Knight(True)
        self.board[7][2] = Bishop(True)
        self.board[7][3] = King(True)
        self.board[7][4] = Queen(True)
        self.board[7][5] = Bishop(True)
        self.board[7][6] = Knight(True)
        self.board[7][7] = Castle(True)
