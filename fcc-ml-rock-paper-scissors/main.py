# main.py
# Run player against all 4 FCC bots

from RPS_game import hafizur, rahman, rony, aishu, play
from RPS import player, reset_player

if __name__ == "__main__":

    reset_player()
    print("Playing against hafizur...")
    print(play(player, hafizur, 1000, verbose=False))

    reset_player()
    print("Playing against rahman...")
    print(play(player, rahman, 1000, verbose=False))

    reset_player()
    print("Playing against rony...")
    print(play(player, rony, 1000, verbose=False))

    reset_player()
    print("Playing against aishu...")
    print(play(player, aishu, 1000, verbose=False))
