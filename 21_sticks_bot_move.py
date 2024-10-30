import random

def bot_move(sticks_left):
    """
    Determins the bot's move baed on the number of sticks left.
    The bot will always try to leave a multiple of 4 sticks for the player.
    """
    if sticks_left % 4 == 0:
        # Randomly pick 1, 2, or 3 if it's already a multiple of 4
        return random.randint(1, 3)
    else:
        # Take enough sticks to leave a multiple of 4 
        return sticks_left % 4
    

def play_game():
    """
    Plays the 21 Sticks game where the bot (Player 1) always wins.
    """
    sticks = 21
    current_player = 1 # Bot starts first

    print("21 sticks in the pile.")

    while sticks > 0:
        if current_player == 1:
            # Bot's turn
            bot_choice = bot_move(sticks)
            sticks -= bot_choice
            print(f"Bot takes: {bot_choice}")
            print(f"{sticks} sticks left in the pile.")
            if sticks == 0:
                print("Bot won!")
                break
        else:
            # Player 2's turn
            player_choice = int(input("Player 2 takes (1-3): "))
            sticks -= player_choice
            print(f"{sticks} sticks left in the pile.")
            if sticks == 0:
                print("Player 2 won!")
                break
        
        current_player = current_player % 2 + 1


if __name__ == "__main__":
    play_game()
