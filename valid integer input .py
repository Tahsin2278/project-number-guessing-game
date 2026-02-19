# Import random module to generate a random number
"""
It will ask the user for a valid integer input
"""
import random


# Function to get a valid integer input with error handling
def valid_integer(prompt: str) -> int:
    try:
        integer = int(input(prompt))
        return integer
    except ValueError:
        print("Please enter a valid integer.")


# Prompt the user for a low and high number to set the guessing range.
"""
It will ask the user to guess a number range and ensure higher number is greater than lower number.
"""
min_num = valid_integer("Enter the minimum number: ")
max_num = valid_integer("Enter the maximum number: ")


def get_range():
    if min_num > max_num:
        print("Please ensure the minimum number is lower than maximum number.")
    elif max_num > min_num:
        print("You chose appropriate number range.")
    else:
        print("You need to choose two different numbers.")


number = get_range()
