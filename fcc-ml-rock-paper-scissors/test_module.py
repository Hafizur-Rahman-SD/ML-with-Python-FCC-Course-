# test_module.py
# Unit tests to check if player wins at least 60% against all bots

import unittest
from RPS_game import hafizur, rahman, rony, aishu, play
from RPS import player

class UnitTests(unittest.TestCase):
    def test_hafizur(self):
        result = play(player, hafizur, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_rahman(self):
        result = play(player, rahman, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_rony(self):
        result = play(player, rony, 1000)
        self.assertGreater(result["Player1"], 590)

    def test_aishu(self):
        result = play(player, aishu, 1000)
        self.assertGreater(result["Player1"], 590)
