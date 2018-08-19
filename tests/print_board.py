#!/usr/bin/env python3

"""
Chess: tests
print_board.py
desc: print the board
vers: 0.0.1
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chess import Game

game = Game()
print(game.board)
