# test_module.py
# Tests to check if player wins at least 60% against all bots

import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class UnitTests(unittest.TestCase):
    def test_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_abbey(self):
        result = play(player, abbey, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_kris(self):
        result = play(player, kris, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_mrugesh(self):
        result = play(player, mrugesh, 1000)
        self.assertGreater(result["Player1"], 590)
