"""
This is a game of dice rolling.
You will roll and the computer will roll.
The winner gets points.
"""

import random


def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def roll_dice() -> int:
    """
    Will return random number.
    """
    min_num = get_number("Choose the minimum value: ")
    max_num = get_number("Choose the maximum value: ")
    randnum = random.randint(min_num, max_num)
    return randnum


def play():
    player_roll = roll_dice()
    computer_roll = roll_dice()
    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        return 1
    elif computer_roll > player_roll:
        return -1
    else:
        return 0


player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    result = play()

    if result == 1:
        player_score += 1
    elif result == -1:
        computer_score += 1

# Print final score and goodbye
print(f"Your score: {player_score}, Computer score: {computer_score}")
print("Bye")
