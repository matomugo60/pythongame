import random

# Generate secret number between 1 and 50
secret_number = random.randint(1, 50)

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 50.")
print("You have 5 attempts.")

# Give the user 5 guesses
for attempt in range(5):
    guess = int(input("\nEnter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number}!")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

# Runs only if the loop wasn't broken
else:
    print(f"\nGame Over! The secret number was {secret_number}.")