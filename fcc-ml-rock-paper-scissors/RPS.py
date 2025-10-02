# RPS.py

def player(prev_play, opponent_history=[]):
    # If opponent made a move last time, save it in the history
    if prev_play != "":
        opponent_history.append(prev_play)

    # If this is the first round, just return "R"
    if len(opponent_history) == 0:
        return "R"

    # Find which move opponent used the most till now
    most_common = max(set(opponent_history), key=opponent_history.count)

    # Play the move that can beat the opponent's most common choice
    if most_common == "R":
        return "P"   # Paper beats Rock
    elif most_common == "P":
        return "S"   # Scissors beats Paper
    else:
        return "R"   # Rock beats Scissors
