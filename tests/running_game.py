#!/usr/bin/env python3

"""
Chess: tests
running_game.py
desc: tests the integrity of a game that has started and is running
vers: 0.0.1
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chess import Game

game = Game()
print(game)
