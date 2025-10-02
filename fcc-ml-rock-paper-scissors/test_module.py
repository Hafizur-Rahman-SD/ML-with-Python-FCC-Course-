# test_module.py
import unittest
from RPS_game import hafizur, rahman, rony, aishu, play
from RPS import player

class UnitTests(unittest.TestCase):
    def test_hafizur(self):
        self.assertGreater(play(player, hafizur, 1000)["Player1"], 590)

    def test_rahman(self):
        self.assertGreater(play(player, rahman, 1000)["Player1"], 590)

    def test_rony(self):
        self.assertGreater(play(player, rony, 1000)["Player1"], 590)

    def test_aishu(self):
        self.assertGreater(play(player, aishu, 1000)["Player1"], 590)

if __name__ == "__main__":
    unittest.main()
