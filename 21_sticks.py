def play_game():
    """
    Starts the game of 21 sticks for two players.

    Each player takes turns removing 1-3 sticks from the pile. 
    The player who takes the last stick loses. The game continues 
    until there are no more sticks left, and the winner is declared.
    """
    total_sticks = 21
    current_player = 1

    print("21 sticks in the pile.")

    # Main game loop
    while total_sticks > 0:
        print(f"Player {current_player} takes: ", end="")
        sticks_taken = int(input())

        # Update the total sticks
        total_sticks -= sticks_taken
        if total_sticks <= 0:
            print("0 sticks in the pile.")
            print(f"Player {current_player} won!")
            break

        print(f"{total_sticks} sticks in the pile.")

        # Switch to the next player
        current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    """
    Entry point for the program.

    Calls the `play_game` function to start the game of 21 sticks
    for two players.
    """
    play_game()
