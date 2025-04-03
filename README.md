# BlackJack Game

A console-based implementation of the classic Blackjack card game, where players aim to beat the dealer by obtaining a hand value closest to 21 without exceeding it.

## Table of Contents

- [Overview](#overview)
- [How to Play](#how-to-play)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

The Blackjack Game is a Python-based console application that simulates the traditional Blackjack card game. Players compete against a computer-controlled dealer, making strategic decisions to hit, stand, or double down in pursuit of a winning hand.

## How to Play

1. **Start the Game**: Run the `BlackJack.py` script to initiate the game.
2. **Receive Initial Cards**: Both the player and dealer are dealt two cards. The player's cards are visible, while one of the dealer's cards remains hidden.
3. **Player's Turn**: Choose to:
   - **Hit**: Draw another card.
   - **Stand**: Keep the current hand.
   - **Double Down**: Double the bet and receive one final card (if applicable).
4. **Dealer's Turn**: The dealer reveals the hidden card and draws additional cards according to the game's rules.
5. **Determine Outcome**: The game compares hand values to declare a winner or identify a tie.
6. **Continue or Exit**: Opt to play another round or exit the game.

## Technologies Used

- **Python**: Core programming language for game logic and execution.

## Lessons Learned

Developing this project provided valuable insights into:

- **Game Logic Development**: Crafting rules and conditions to accurately simulate Blackjack gameplay.
- **User Input Handling**: Managing and validating user inputs to ensure a smooth gaming experience.
- **Randomization**: Utilizing Python's `random` module to shuffle the deck and deal cards unpredictably.
- **Error Handling**: Anticipating and managing potential errors, such as invalid inputs or edge cases in gameplay.

