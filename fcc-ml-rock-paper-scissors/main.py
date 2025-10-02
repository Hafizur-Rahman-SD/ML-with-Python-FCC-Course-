# main.py
# Test player against all sample bots

from RPS_game import hafizur, rahman, rony, aishu, play
from RPS import player

if __name__ == "__main__":
    print("Playing against hafizur...")
    print(play(player, hafizur, 1000, verbose=False))

    print("Playing against rahman...")
    print(play(player, rahman, 1000, verbose=False))

    print("Playing against rony...")
    print(play(player, rony, 1000, verbose=False))

    print("Playing against aishu...")
    print(play(player, aishu, 1000, verbose=False))
