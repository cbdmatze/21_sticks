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
    