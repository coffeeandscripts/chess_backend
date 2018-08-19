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

    def move(self, start, finish, user):
        x_start = int(ord(start[0].lower())-97)
        y_start = 8-int(start[1])
        x_finish = int(ord(finish[0].lower())-97)
        y_finish = 8-int(finish[1])
        piece = self.board[y_start][x_start]
        if x_start == x_finish and y_start == y_finish:
            return 0 
        if piece != " " and piece.check_movement((y_start, x_start), (y_finish, x_finish), self):
            if user != piece.user:
                return 0
            self.board[y_finish][x_finish] = self.board[y_start][x_start]
            self.board[y_start][x_start] = " "
            return 1
        else:
            return 0

    def occupied(self, enemy, y, x, user):
        occupied = True
        piece = self.board[y][x]
        if piece != " ":
            if enemy:
                if piece.user == user:
                    occupied = False
        else:
            occupied = False
        return occupied

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
