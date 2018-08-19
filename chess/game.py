#!/usr/bin/env python3

"""
Chess
game.py
desc: classes to define a running game
vers: 0.0.1
"""

from datetime import datetime

class Game:
    def __init__(self):
        self.start_time = datetime.now()
        self.last_updated = datetime.now()

    def __str__(self):
        return ("Chess: game started at " + str(self.start_time))
