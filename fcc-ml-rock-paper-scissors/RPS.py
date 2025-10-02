# RPS.py
# Fully deterministic Rock-Paper-Scissors bot
# Works against FCC bots: hafizur, rahman, rony, aishu

def counter(move):
    """Return the move that beats the given move"""
    if move == "R":
        return "P"
    elif move == "P":
        return "S"
    else:
        return "R"

def player(prev_play):
    """Return next move based on opponent's last move"""
    # Initialize history and cycle
    if not hasattr(player, "opponent_history"):
        player.opponent_history = []
        player.my_history = []
        player.cycle_index = 0
        player.cycle_moves = ["R", "P", "S"]

    if prev_play == "":
        move = "R"
        player.my_history.append(move)
        return move

    # Save opponent move
    player.opponent_history.append(prev_play)
    last_opponent = player.opponent_history[-1]

    # Default strategy: counter last move
    move = counter(last_opponent)

    # Reactive bot handling
    if len(player.my_history) >= 1:
        last_my = player.my_history[-1]
        if last_opponent == counter(last_my):
            move = player.cycle_moves[player.cycle_index % 3]
            player.cycle_index += 1

    player.my_history.append(move)
    return move

def reset_player():
    """Clear history and cycle for fresh match"""
    for attr in ["opponent_history", "my_history", "cycle_index", "cycle_moves"]:
        if hasattr(player, attr):
            delattr(player, attr)
