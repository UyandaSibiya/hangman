# Hangman Game

Welcome to the Hangman Game! This project is a console-based Python game where players try to guess a hidden word by guessing one letter at a time. It’s simple, engaging, and has customizable settings to increase or decrease the challenge!

## Game Overview

In Hangman, the objective is to guess the letters of a hidden word before running out of attempts. Each incorrect guess brings the player closer to "hanging" the man. The game ends when the player either successfully guesses all letters in the word or exhausts all attempts.

## Features

- **Difficulty Levels**: Players can select from easy, medium, or hard levels. The difficulty affects both the number of attempts and the word length.
- **Hints**: Limited hints are available, revealing one letter in exchange for an attempt.
- **Scoring System**: Points are awarded for correct guesses and deducted for incorrect guesses, adding a competitive element to the game.
- **ASCII Art**: A Hangman figure is drawn step-by-step as attempts decrease, providing visual feedback.
- **Colorful Messages**: Using the `colorama` library, the game highlights correct guesses, incorrect guesses, hints, and status updates in different colors.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. You’ll also need the `colorama` library for colorful text output. Install it with:

```bash
pip install colorama



Setting Up
    Clone the Repository
    bash

git clone <repository-url>
cd hangman-game


Run the Game
Start the game by running:

bash
python hangman.py


How to Play

    Select Difficulty:
        Easy: Short words, 8 attempts.
        Medium: Medium-length words, 6 attempts.
        Hard: Longer words, 4 attempts.

    Guess Letters: Type letters to guess parts of the hidden word. If your guess is correct, the letter appears in the word; if not, attempts are reduced.

    Using Hints:
        Type "hint" during your turn to reveal one letter.
        You can only use one hint per game, and it will cost an attempt.

    Scoring:
        +10 points for each correct guess.
        -5 points for each incorrect guess.
        Your score is shown at the end of the game.

    ASCII Hangman: Watch the Hangman figure appear with each wrong guess, adding suspense as you approach the final attempt.

Game Rules

    Each guess should be a single letter (case-insensitive).
    Repeated guesses are allowed but will prompt a reminder if the letter was already guessed.
    To win, correctly guess all letters of the word within the allowed attempts.
    The game ends in a loss if all attempts are exhausted before completing the word.

