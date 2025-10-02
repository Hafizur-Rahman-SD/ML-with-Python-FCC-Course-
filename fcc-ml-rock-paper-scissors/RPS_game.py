# RPS_game.py
# This file contains the game engine and some sample bots.
# Do not change this file.

import random

def play(player1, player2, num_games, verbose=False):
    # Keep track of scores
    p1_wins = 0
    p2_wins = 0
    ties = 0
    prev1 = ""
    prev2 = ""

    # Loop through all games
    for i in range(num_games):
        # Get moves from both players
        p1 = player1(prev2)
        p2 = player2(prev1)

        # Decide winner for this round
        if p1 == p2:
            ties += 1
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_wins += 1
        else:
            p2_wins += 1

        # Update previous plays for next round
        prev1 = p1
        prev2 = p2

        # Print details if verbose is True
        if verbose:
            print(f"Game {i+1}: Player1={p1}, Player2={p2}")

    # Return final result
    return {"Player1": p1_wins, "Player2": p2_wins, "Ties": ties}


# Sample bot that repeats a fixed pattern
def quincy(prev_play, opponent_history=[]):
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(opponent_history) % len(choices)]


# Sample bot that reacts to last opponent move
def abbey(prev_play, opponent_history=[]):
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)

    # If opponent played Rock last time, return Paper
    if opponent_history[-1] == "R":
        return "P"
    else:
        return "S"


# Sample bot that cycles through choices
def kris(prev_play, opponent_history=[]):
    choices = ["R", "R", "P", "P", "S", "S"]
    return choices[len(opponent_history) % len(choices)]


# Sample bot that copies last move of opponent
def mrugesh(prev_play, opponent_history=[]):
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    return opponent_history[-1]
