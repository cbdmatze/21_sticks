Certainly! Below are two `README.md` files for both versions of the program: **without the bot** and **with the bot**.

---

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
   python3 21_sticks.py
   ```

Enjoy the challenge against the unbeatable bot!

---

In both `README.md` files, make sure to replace the URL in the `git clone` command with the actual URL of your repository. These readme files outline the rules, provide a brief example, and include setup instructions for users.