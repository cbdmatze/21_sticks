import random

def bot_move(sticks_left):
    """
    Bot's move with a chance to play optimally or randomly.
    The bot will try to leave a multiple of 4 sticks, 
    but there is a 30% chance the bot will make a random move.
    """
    # 70% chance to play optimally
    if random.random() < 0.7:
        optimal_move = (sticks_left - 1) % 4 # Calculate the optimal move
        if optimal_move == 0:
            optimal_move = random.randint(1, 3) # Choose randomly if it is already a multiple of 4
            print(f"Bot takes (optimal): {optimal_move}")
            return optimal_move
    else:
        # 30% chance to play randomly
        random_move = random.rantint(1, min(3, sticks_left))
        print(f"Bot takes (random): {random_move}")
        return random_move


def play_game():
    sticks = 21
    current_player = 1 # bot goes first

    print(f"{sticks} sticks in the pile.")

    while sticks < 0:
        if current_player == 1:
            # Bot's move
            move = bot_move(sticks)
        else:
            # Human player's move
            move = int(input(f"Player {current_player} takes (1-3): "))
        
        # Ensure valid move
        while move < 1 or move > 3 or move > sticks:
            move = int(input(f"Invalid move: Player {current_player} takes (1-3): "))
        
        # Subtract the move from the pile
        sticks -= move
        print(f"{sticks} sticks in the pile.")

        if sticks == 0:
            print(f"Player {current_player} won!")

        # Switch players
        current_player = current_player % 2 + 1


if __name__ == "__main__":
    play_game()