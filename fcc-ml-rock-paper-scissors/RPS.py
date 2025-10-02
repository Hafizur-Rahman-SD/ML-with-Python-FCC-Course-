# RPS.py
# Improved Rock-Paper-Scissors bot
# This bot uses multiple strategies to beat all opponents.

import random

def player(prev_play, opponent_history=[], my_history=[]):
    # Save opponent's last move
    if prev_play != "":
        opponent_history.append(prev_play)

    # Save my last move
    if len(my_history) > 0:
        last_my_move = my_history[-1]
    else:
        last_my_move = None

    # First move, just play Rock
    if len(opponent_history) == 0:
        my_move = "R"
        my_history.append(my_move)
        return my_move

    # Count frequency of opponent moves
    count_R = opponent_history.count("R")
    count_P = opponent_history.count("P")
    count_S = opponent_history.count("S")

    # Strategy 1: Beat most frequent move
    if count_R > count_P and count_R > count_S:
        my_move = "P"  # Paper beats Rock
    elif count_P > count_R and count_P > count_S:
        my_move = "S"  # Scissors beats Paper
    elif count_S > count_R and count_S > count_P:
        my_move = "R"  # Rock beats Scissors
    else:
        # Strategy 2: If opponent is copying last move (mrugesh), play move that beats opponent last
        last_opponent = opponent_history[-1]
        if last_opponent == "R":
            my_move = "P"
        elif last_opponent == "P":
            my_move = "S"
        else:
            my_move = "R"

    # Save my move for next round
    my_history.append(my_move)
    return my_move
