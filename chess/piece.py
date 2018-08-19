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
            
    def check_movement(self, start, finish, board):
        valid_move = True
        if self.user:
            if start[0] == 6:
                if start[0] - finish[0] > 2:
                    valid_move = False
            else:
                if start[0] - finish[0] > 1:
                    valid_move = False
            if start[0] - finish[0] == 1 and (start[1] - finish[1] == 1 or start[1] - finish[1] == -1):
                if not board.occupied(1, finish[0], finish[1], self.user):
                    valid_move = False
            if start[1] == finish[1]:
                for y in range(finish[0], start[0]):
                    if board.occupied(0, y, finish[1], self.user):
                        valid_move = False
        else:
            if start[0] == 1:
                if finish[0] - start[0] > 2:
                    valid_move = False
            else:
                if finish[0] - start[0] > 1:
                    valid_move = False
            if finish[0] - start[0] == 1 and (start[1] - finish[1] == 1 or start[1] - finish[1] == -1):
                if not board.occupied(1, finish[0], finish[1], self.user):
                    valid_move = False
            if start[1] == finish[1]:
                for y in range(finish[0], start[0]):
                    if board.occupied(0, y, finish[1], self.user):
                        valid_move = False
        return valid_move
        
class Castle:
    def __init__(self, res):
        self.user = res
        self.char = "H"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
            
    def check_movement(self, start, finish, board):
        pass

class Knight:
    def __init__(self, res):
        self.user = res
        self.char = "Y"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
            
    def check_movement(self, start, finish, board):
        pass

class Bishop:
    def __init__(self, res):
        self.user = res
        self.char = "B"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
            
    def check_movement(self, start, finish, board):
        pass

class Queen:
    def __init__(self, res):
        self.user = res
        self.char = "Q"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
            
    def check_movement(self, start, finish, board):
        pass

class King:
    def __init__(self, res):
        self.user = res
        self.char = "K"

    def __str__(self):
        if self.user:
            return self.char
        else:
            return self.char.lower()
            
    def check_movement(self, start, finish, board):
        pass
