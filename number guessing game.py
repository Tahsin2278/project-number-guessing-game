# Import random module to generate a random number
import random

"""
Number Guessing Game
Description:
This program asks the user to guess a randomly generated number
within a user-defined range and limited number of attempts.
"""


# --------------------------------------------------
# Function to get a valid integer input with error handling
# Uses try/except and .strip() to prevent crashes
# --------------------------------------------------
def valid_integer(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print(" Please enter a valid integer.")


# --------------------------------------------------
# Function to get a valid 'y' or 'n' response from the user
# Keeps asking until correct input is provided
# --------------------------------------------------
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# --------------------------------------------------
# Function to play one round of the game
# --------------------------------------------------
def play_game():
    # Ask for user's name and greet them
    name = input("Enter your name: ").strip().title()
    print(f"\n Welcome, {name}! Let's play the Number Guessing Game ")

    # Ask for number range
    low_number = valid_integer("Enter the LOW number: ")
    high_number = valid_integer("Enter the HIGH number: ")

    # Ensure low_number is less than high_number
    while high_number <= low_number:
        print(" High number must be greater than low number.")
        high_number = valid_integer("Enter the HIGH number again: ")
    # Ask for number of attempts
    max_attempts = valid_integer("How many attempts do you want?")
    # Generate random number
    secret_number = random.randint(low_number, high_number)
    # Track number of attempts
    attempts_used = 0
    print(f"\n I have chosen a number between {low_number} and {high_number}.")
    print("Try to guess it!")
    # Loop for user guesses
    while attempts_used < max_attempts:
        guess = valid_integer(f"\nAttempt {attempts_used + 1} of {max_attempts}: ")
        attempts_used += 1
        # Check if guess is too low or too high
        if guess < secret_number:
            print(" Too low!")
        elif guess > secret_number:
            print(" Too high!")
        else:
            # Display success message if guessed correctly
            print(
                f"\n Congratulations {name}! "
                f"You guessed the number in {attempts_used} attempts."
            )
            return

    # If max attempts are used up, reveal the correct number
    print(f"\n Out of attempts! The correct number was {secret_number}.")


# --------------------------------------------------
# Main game loop
# --------------------------------------------------
while True:
    play_game()

    # Ask if they want to play again, only accepting 'y' or 'n'
    if not get_yes_no("\nDo you want to play again? (y/n): "):
        print("\n Goodbye! Thanks for playing.")
        break

# Run the game
