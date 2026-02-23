# Import random module to generate a random number
"""
Asks user to put a valid integer input, handling errors.
"""
import random
# Function to get a valid integer input with error handling
def valid_integer(prompt:str)->int:
    while True:
        try:
            integer=int(input(prompt))
            return integer
        except ValueError:
            print("please enter a valid integer.")
print("Welcome to the number guessing game. \n You can choose any number range you want. \n You will be given a limited number of attempts to choose the number. \n After maximum attempts are used, correct number will be revealed. \n Enjoy the game!")
# Function to get the minimum number and maximum number from user
def get_range():
    min_num= valid_integer("Enter the minimum number: ")
    return min_num
    max_num= valid_integer("Enter the maximum number: ")
    return max_num
random_number= random.randint(min_num, max_num)
number= get_range()
