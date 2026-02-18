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


def roll_dice(min_num: int, max_num: int) -> int:
    """
    Will return random number.
    """
    random_number = random.randint(min_num, max_num)


def play(min_num: int, max_num: int) -> int:
    player_roll = roll_dice(min_num, max_num)
    computer_roll = roll_dice(min_num, max_num)
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
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))
while player_score < 3 and computer_score < 3:
    result = play(min_num, max_num)
    if result == 1:
        player_score += 1
    elif result == -1:
        computer_score += 1

# Print final score and goodbye
print(f"Your score: {player_score}, Computer score: {computer_score}")
print("Bye")
