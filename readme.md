

### **README for the "21 Sticks" Game (Without Bot)**

# 21 Sticks Game

This is a simple two-player game called **21 Sticks**. The goal of the game is for two players to take turns removing sticks from a pile, and the player who is forced to take the last stick loses the game.

## How to Play

- The game starts with 21 sticks in the pile.
- Players take turns, with each player choosing to take 1, 2, or 3 sticks on their turn.
- The game continues until there are no sticks left.
- The player who is forced to take the last stick loses the game.

## Example Gameplay

```bash
$ python3 21_sticks.py
21 sticks in the pile.
Player 1 takes: 2
19 sticks in the pile.
Player 2 takes: 3
16 sticks in the pile.
Player 1 takes: 3
13 sticks in the pile.
Player 2 takes: 1
12 sticks in the pile.
...
Player 2 takes: 3
0 sticks in the pile.

Player 2 won!
```

## Requirements

- Python 3.x

## Running the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/21_sticks.git
   ```
2. Navigate to the project folder:
   ```bash
   cd 21_sticks
   ```
3. Run the game:
   ```bash
   python3 21_sticks.py
   ```

Enjoy the game!

---

### **README for the "21 Sticks" Game (With Bot)**

# 21 Sticks Game - Bot Edition

This is an enhanced version of the **21 Sticks** game where **Player 1 is a bot**. The bot is programmed to play optimally and always win if it plays first.

## How to Play

- The game starts with 21 sticks in the pile.
- Player 1 is controlled by a bot, while Player 2 is controlled by a human player.
- On each turn, players (including the bot) can take 1, 2, or 3 sticks from the pile.
- The bot will always make a move that maximizes its chances of winning by following a strategy.
- The game continues until there are no sticks left.
- The player who is forced to take the last stick loses the game.

## How the Bot Works

The bot aims to leave a number of sticks that is a **multiple of 4** after its move, forcing the human player into a losing position. If the number of sticks left is already a multiple of 4, the bot will randomly take 1, 2, or 3 sticks to disrupt the player's strategy.

## Example Gameplay

```bash
$ python3 21_sticks.py
21 sticks in the pile.
Bot takes: 1
20 sticks in the pile.
Player 2 takes (1-3): 3
17 sticks in the pile.
Bot takes: 1
16 sticks in the pile.
Player 2 takes (1-3): 2
14 sticks in the pile.
Bot takes: 2
12 sticks in the pile.
...
Bot takes: 3
0 sticks in the pile.

Bot won!
```

## Requirements

- Python 3.x

## Running the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/21_sticks.git
   ```
2. Navigate to the project folder:
   ```bash
   cd 21_sticks
   ```
3. Run the game:
   ```bash
   python3 21_sticks_bot_move.py
   ```

Enjoy the challenge against the unbeatable bot!



To add a twist that gives the human player a chance to prevent the bot from winning, we could modify the bot's strategy. Instead of making the bot always play optimally, we can randomize the bot's moves sometimes, so it's not always perfect. This makes the game more unpredictable, giving the human player a chance to win.

### Twist: Random Moves for the Bot

Here's an idea:
- On the bot's turn, it has a chance (say 30%) of making a **random move**, instead of an optimal one.
- This random move could disrupt the bot's strategy, creating an opportunity for the human player to win.

#### Updated Logic for the Bot's Move:
1. **Optimal move (70% chance)**: The bot plays the strategy where it tries to leave a multiple of 4 sticks after its turn.
2. **Random move (30% chance)**: The bot randomly picks 1, 2, or 3 sticks, which could be a non-optimal move.

Here's how you could modify the game with this twist:

---

### Updated Python Code with a Twist

```python
import random

def bot_move(sticks_left):
    """
    Bot's move with a chance to play optimally or randomly.
    The bot will try to leave a multiple of 4 sticks, but there is
    a 30% chance it will make a random move.
    """
    # 70% chance to play optimally
    if random.random() < 0.7:
        optimal_move = (sticks_left - 1) % 4  # Calculate the optimal move
        if optimal_move == 0:
            optimal_move = random.randint(1, 3)  # Choose randomly if it's already a multiple of 4
        print(f"Bot takes (optimal): {optimal_move}")
        return optimal_move
    else:
        # 30% chance to play randomly
        random_move = random.randint(1, min(3, sticks_left))
        print(f"Bot takes (random): {random_move}")
        return random_move

def play_game():
    sticks = 21
    current_player = 1  # Bot goes first

    print(f"{sticks} sticks in the pile.")
    
    while sticks > 0:
        if current_player == 1:
            # Bot's move
            move = bot_move(sticks)
        else:
            # Human player's move
            move = int(input(f"Player {current_player} takes (1-3): "))

        # Ensure valid move
        while move < 1 or move > 3 or move > sticks:
            move = int(input(f"Invalid move! Player {current_player} takes (1-3): "))
        
        # Subtract the move from the pile
        sticks -= move
        print(f"{sticks} sticks in the pile.")

        if sticks == 0:
            print(f"Player {current_player} won!")
            break

        # Switch players
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()
```

### Explanation of Changes:
1. **`bot_move(sticks_left)`**: The bot has a 70% chance to play optimally and a 30% chance to pick a random number of sticks. This randomness introduces unpredictability and gives the human player a fighting chance.
2. **`random.random() < 0.7`**: Determines if the bot plays optimally (70% chance).
3. **`random.randint(1, 3)`**: When the bot makes a random move, it chooses between 1 and 3 sticks.

### Example Gameplay:

```bash
$ python3 21_sticks.py
21 sticks in the pile.
Bot takes (random): 2
19 sticks in the pile.
Player 2 takes (1-3): 3
16 sticks in the pile.
Bot takes (optimal): 3
13 sticks in the pile.
Player 2 takes (1-3): 2
11 sticks in the pile.
Bot takes (random): 1
10 sticks in the pile.
Player 2 takes (1-3): 3
7 sticks in the pile.
...
Player 2 takes (1-3): 1
0 sticks in the pile.

Player 2 won!
```

In this case, the human player managed to win due to the bot occasionally making random moves.

---

### **Updated README with the Twist**

# 21 Sticks Game - Bot Edition (With a Twist!)

This is a fun version of the **21 Sticks** game where **Player 1 is a bot**. Unlike the original version, this bot does not always play optimally. There's a chance for the human player to win, as the bot might make random moves!

## How to Play

- The game starts with 21 sticks in the pile.
- Player 1 is controlled by a bot, while Player 2 is controlled by a human player.
- On each turn, players (including the bot) can take 1, 2, or 3 sticks from the pile.
- The bot usually plays optimally, trying to leave a multiple of 4 sticks, but **sometimes it plays randomly**, giving the human player a chance to win.
- The game continues until there are no sticks left.
- The player who is forced to take the last stick loses the game.

## How the Bot Works

The bot has a 70% chance of playing optimally and a 30% chance of playing randomly. This random element creates an exciting twist that gives the human player a better chance of winning.

## Example Gameplay

```bash
$ python3 21_sticks.py
21 sticks in the pile.
Bot takes (random): 2
19 sticks in the pile.
Player 2 takes (1-3): 3
16 sticks in the pile.
Bot takes (optimal): 3
13 sticks in the pile.
Player 2 takes (1-3): 2
11 sticks in the pile.
Bot takes (random): 1
10 sticks in the pile.
Player 2 takes (1-3): 3
7 sticks in the pile.
...
Player 2 takes (1-3): 1
0 sticks in the pile.

Player 2 won!
```

## Requirements

- Python 3.x

## Running the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/21_sticks.git
   ```
2. Navigate to the project folder:
   ```bash
   cd 21_sticks
   ```
3. Run the game:
   ```bash
   python3 21_sticks_bot_twist.py
   ```

---

This twist introduces an element of unpredictability, making the game more engaging and giving the human player a fighting chance!
