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


def range():
    min_num = valid_integer("Enter the minimum number: ")
    max_num = valid_integer("Enter the maximum number: ")
