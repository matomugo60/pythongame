# Guess the Number Game

A simple command-line game built with Python where players try to guess a randomly generated number within a limited number of attempts.

This project introduces fundamental Python concepts including loops, conditionals, user input, random number generation, and type casting.

---

## Features

* Randomly generates a secret number between 1 and 50
* Gives the player 5 attempts to guess correctly
* Provides feedback after each guess:

  * Too high
  * Too low
  * Correct guess
* Reveals the secret number if all attempts are used
* Simple command-line interface

---

## Technologies Used

* Python 3
* Python's built-in `random` module

No external libraries are required.

---

## Project Structure

```plaintext
project-folder/
│
└── game.py
```

---

## How It Works

1. The program generates a random number between 1 and 50.
2. The player is given 5 attempts to guess the number.
3. After each guess:

   * The game indicates whether the guess was too high or too low.
   * If the guess is correct, the game ends with a congratulatory message.
4. If all attempts are exhausted, the game reveals the secret number.

---

## Concepts Practiced

### Importing Modules

```python
import random
```

Allows access to Python's random number generation functions.

---

### Random Number Generation

```python
secret_number = random.randint(1, 50)
```

Generates a random integer between 1 and 50.

---

### Loops

```python
for attempt in range(5):
```

Runs the guessing logic five times.

---

### Conditional Statements

```python
if guess == secret_number:
    print("You win!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")
```

Used to compare the player's guess to the secret number.

---

### Type Casting

```python
guess = int(input("Enter your guess: "))
```

Converts user input from a string into an integer.

---

### f-Strings

```python
print(f"The secret number was {secret_number}")
```

Allows variables to be embedded directly inside strings.

---

## Installation

### Prerequisites

Make sure Python 3 is installed.

Check your version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Running the Game

Navigate to the project directory:

```bash
cd guess-the-number
```

Run the game:

```bash
python game.py
```

or

```bash
python3 game.py
```

---

## Example Gameplay

```plaintext
Welcome to Guess the Number!
I'm thinking of a number between 1 and 50.
You have 5 attempts.

Enter your guess: 20
Too low! Try again.

Enter your guess: 35
Too high! Try again.

Enter your guess: 27
Congratulations! You guessed the number 27!
```

---

## Learning Objectives

This project helps reinforce:

* Python syntax and indentation
* Importing modules
* Loops with `range()`
* Conditional logic
* User input handling
* Type conversion
* String formatting with f-strings

---

## Future Improvements

Potential enhancements include:

* Input validation using `try` and `except`
* Difficulty levels (Easy, Medium, Hard)
* Multiple rounds and replay option
* Score tracking
* High score system
* Hint system
* Graphical interface using Tkinter or Pygame

---

## Author

Martin Mugo

---
