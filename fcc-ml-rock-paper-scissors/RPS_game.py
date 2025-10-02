# RPS_game.py
# Game logic and sample bots
# Do not modify this file

import random

def play(player1, player2, num_games, verbose=False):
    p1_wins = 0
    p2_wins = 0
    ties = 0
    prev1 = ""
    prev2 = ""

    for i in range(num_games):
        p1 = player1(prev2)
        p2 = player2(prev1)

        if p1 == p2:
            ties += 1
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_wins += 1
        else:
            p2_wins += 1

        prev1 = p1
        prev2 = p2

        if verbose:
            print(f"Game {i+1}: Player1={p1}, Player2={p2}")

    return {"Player1": p1_wins, "Player2": p2_wins, "Ties": ties}


# Sample bots
def quincy(prev_play, opponent_history=[]):
    # Cycles through fixed pattern
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(opponent_history) % len(choices)]

def abbey(prev_play, opponent_history=[]):
    # Reactive bot
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    if opponent_history[-1] == "R":
        return "P"
    else:
        return "S"

def kris(prev_play, opponent_history=[]):
    # Cycles repeated moves
    choices = ["R", "R", "P", "P", "S", "S"]
    return choices[len(opponent_history) % len(choices)]

def mrugesh(prev_play, opponent_history=[]):
    # Copies last move of opponent
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    return opponent_history[-1]
