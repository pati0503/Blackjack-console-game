# Blackjack Game

Simple console implementation of the Blackjack card game written in Python.

The program simulates a standard Blackjack round between a player and a dealer.  
The player can draw cards, the dealer follows standard rules, and the winner is determined according to Blackjack scoring logic.

## Features

- Random card dealing
- Player can draw multiple cards
- Dealer draws cards until reaching 17 points
- Automatic Ace handling (11 or 1)
- Blackjack detection (21 with two cards)
- Bust detection (score over 21)
- Final score comparison and result display

## Game Rules Implemented

- Blackjack is detected when a player gets 21 with exactly two cards
- Ace counts as 11 by default, but changes to 1 if total score exceeds 21
- Dealer draws cards until score is at least 17
- Player can continue drawing cards until choosing to stop or busting
- Special handling for Blackjack outcomes

## Technologies

- Python 3
- Standard library (`random`)
- Simple console input/output

## How to Run

```bash
python main.py
