#!/usr/bin/env python3

"""
Chess
board.py
desc: classes to define the arrangement of the board
vers: 0.0.1
"""

class Board:
    def __init__(self):
        self.board = [[0]*8]*8;

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
                txt += " * |"
            txt += " " + str(c) + "\n"
            if c > 1:
                txt += "   |-------------------------------|\n"
            c -= 1
        return txt
                

    def print_bottom_line(self):
        return ("   +-------------------------------+\n     A   B   C   D   E   F   G   H")
