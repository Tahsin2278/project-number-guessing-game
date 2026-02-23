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
    name = input("Enter your name: ").strip()
    print(f"\n Welcome, {name}! Let's play the Number Guessing Game ")

    # Ask for number range
    low_number = valid_integer("Enter the LOW number: ")
    high_number = valid_integer("Enter the HIGH number: ")

    # Ensure low_number is less than high_number
    while high_number <= low_number:
        print(" High number must be greater than low number.")
        high_number = valid_integer("Enter the HIGH number again: ")

    