# test_module.py
# This file contains tests to check if the player bot
# can beat other bots with at least 60% win rate.

import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class UnitTests(unittest.TestCase):
    def test_quincy(self):
        # Player should win against quincy at least 60% of the time
        result = play(player, quincy, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_abbey(self):
        # Player should win against abbey at least 60% of the time
        result = play(player, abbey, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_kris(self):
        # Player should win against kris at least 60% of the time
        result = play(player, kris, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_mrugesh(self):
        # Player should win against mrugesh at least 60% of the time
        result = play(player, mrugesh, 1000)
        self.assertGreater(result["Player1"], 590)
