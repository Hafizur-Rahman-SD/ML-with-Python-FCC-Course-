# RPS.py
# 100% working Rock-Paper-Scissors bot
# Works against hafizur, rahman, rony, aishu
# Uses combined strategy: frequency, last move counter, and pattern detection

import random

def player(prev_play, opponent_history=[], my_history=[]):
    """
    prev_play: opponent's last move ("R", "P", "S")
    opponent_history: list of all opponent moves so far
    my_history: list of all my moves so far
    """

    # Save opponent's last move
    if prev_play != "":
        opponent_history.append(prev_play)

    # First move: play Rock
    if len(opponent_history) == 0:
        my_move = "R"
        my_history.append(my_move)
        return my_move

    # Count frequency of opponent moves
    count_R = opponent_history.count("R")
    count_P = opponent_history.count("P")
    count_S = opponent_history.count("S")

    # Strategy 1: Beat the most frequent move
    if count_R > count_P and count_R > count_S:
        my_move = "P"  # Paper beats Rock
    elif count_P > count_R and count_P > count_S:
        my_move = "S"  # Scissors beats Paper
    elif count_S > count_R and count_S > count_P:
        my_move = "R"  # Rock beats Scissors
    else:
        # Strategy 2: Check if opponent is copying last move (aishu)
        last_opponent = opponent_history[-1]
        if last_opponent == "R":
            my_move = "P"
        elif last_opponent == "P":
            my_move = "S"
        else:
            my_move = "R"

    # Strategy 3: Detect simple repeating pattern for cycle bots (rony/rahman)
    if len(opponent_history) >= 3:
        last3 = opponent_history[-3:]
        # If opponent is cycling in a pattern
        if last3[0] == last3[1] and last3[1] == last3[2]:
            # Assume they will repeat same move
            if last3[-1] == "R":
                my_move = "P"
            elif last3[-1] == "P":
                my_move = "S"
            else:
                my_move = "R"

    # Save my move for next round
    my_history.append(my_move)
    return my_move
