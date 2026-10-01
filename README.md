# Number Guessing Game

A command-line number guessing game written in Python. The computer picks a random number between 1 and 100, and you have 7 attempts to guess it. After each guess you get a hint telling you whether your guess was too high or too low.

## Features

- Random number between 1 and 100 on every run
- 7 attempts to guess the number
- "Too high" / "Too low" hints after each guess
- Input validation: non-numbers and out-of-range guesses don't use up an attempt
- Shows the correct number if you run out of attempts
- Tells you how many attempts it took when you win

## How to play

1. Run the program.
2. Enter a number between 1 and 100.
3. Use the hint to adjust your next guess.
4. Find the number before your 7 attempts run out.

## Example

```
Welcome to Number Guessing Game!

I have selected a number between 1 and 100.
You have 7 attempts to guess it.

Attempt 1/7 - Enter your guess: 50
Too High! Try a lower number.

Attempt 2/7 - Enter your guess: 25
Too Low! Try a higher number.

Attempt 3/7 - Enter your guess: 37

Congratulations! You guessed the correct number!
You guessed it in 3 attempt(s).
```

## Run it locally

```bash
git clone https://github.com/sw-arick/number-guessing-game.git
cd number-guessing-game
python number_guessing_game.py
```

Requires Python 3. No external libraries needed.

## Concepts used

- `random` module for generating the secret number
- Recursion for the game loop (`playGame` calls itself for each attempt)
- `try` / `except` for handling invalid input
- A `lambda` function to compare the guess with the secret number
- Functions to keep the code organized

## Ideas for improvement

- Add a "play again" option
- Add difficulty levels (different ranges and attempt counts)
- Track a best score across games
- Let the computer guess your number using binary search

## Author

[sw-arick](https://github.com/sw-arick)
