# RPS_game.py
# Game engine and sample bots
# Do not modify this file for FCC challenge

def play(player1, player2, num_games, verbose=False):
    """
    Run a match between two players for num_games.
    Returns a dictionary with number of wins and ties.
    """
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

# -----------------------------
# Sample bots

def hafizur(prev_play, opponent_history=None):
    """Cyclic pattern bot"""
    if opponent_history is None:
        opponent_history = []
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(opponent_history) % len(choices)]

def rahman(prev_play, opponent_history=None):
    """Reactive bot: plays counter to last opponent move"""
    if opponent_history is None:
        opponent_history = []
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    if opponent_history[-1] == "R":
        return "P"
    elif opponent_history[-1] == "P":
        return "S"
    else:
        return "R"

def rony(prev_play, opponent_history=None):
    """Repeated cycle bot"""
    if opponent_history is None:
        opponent_history = []
    choices = ["R", "R", "P", "P", "S", "S"]
    return choices[len(opponent_history) % len(choices)]

def aishu(prev_play, opponent_history=None):
    """Copy bot: copies opponent's last move"""
    if opponent_history is None:
        opponent_history = []
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    return opponent_history[-1]
