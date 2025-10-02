# main.py
# This file is used for testing the player function
# against different bots.

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player
import unittest
import test_module

if __name__ == "__main__":
    # Play 1000 games against each bot and print results
    print("Playing against quincy...")
    print(play(player, quincy, 1000, verbose=False))

    print("Playing against abbey...")
    print(play(player, abbey, 1000, verbose=False))

    print("Playing against kris...")
    print(play(player, kris, 1000, verbose=False))

    print("Playing against mrugesh...")
    print(play(player, mrugesh, 1000, verbose=False))

    # Uncomment this line to run unit tests automatically
    # unittest.main(module=test_module, exit=False)
