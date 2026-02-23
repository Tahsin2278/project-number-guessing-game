"""
Making a number guessing game with rounds, where the user can select a number range and the number of attempts they want.
The game will give feedback on whether the guess is too high, too low, or correct.
After each round, the user will be asked if they want to play again.
The game will continue until the user decides to stop playing.
"""

# imported a random number to generate a random number
import random


# function for getting an  integer from the user
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


# function to get a valid yes/no response
def get_valid_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice == "y" or choice == "n":
            return choice
        else:
            print("Please enter 'y' for yes or 'n' for no.")


# A FUNCTION THAT PLAYS one RoUND only
def play_game():
    # ask them to select a number range
    low = get_valid_int("Enter the lowest number of the range: ")
    high = get_valid_int("Enter the highest number of the range: ")

    # make sure that that the range is valid
    while high <= low:
        print(
            "Invalid range. The highest number must be greater than the lowest number."
        )
        high = get_valid_int("Enter the highest number of the range: ")

    # gonna ask for attempts
    max_attempts = get_valid_int("How many attempts do you want? ")

    # generate a random number
    secret_number = random.randint(low, high)
    # the number of attempts used
    attempts_used = 0

    # the game loop
    while attempts_used < max_attempts:
        guess = get_valid_int("Enter your guess: ")
        attempts_used += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(
                f"Congratulations! You guessed the number in {attempts_used} attempts."
            )
            return

    # if user runs out of attempts
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")


# gonna ask for their name
name = input("What's your name? ").strip()
print(f"Welcome to the Number Guessing Game, {name}!")

while True:
    play_game()
    # ask if they want to play again
    again = get_valid_yes_no("Do you want to play again? (y/n): ")
    # keep playing and asking until they say no
    if again == "n":
        print("Thanks for playing! Goodbye!")
        # break the loop to end the game and print the message
        break
