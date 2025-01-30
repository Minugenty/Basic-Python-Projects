''' 
This is a simple code to implement the Number guessing game in python.
'''

from math import log
import random

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
number = random.randint(lower_range, upper_range)

chances = int(log(upper_range - lower_range, 2) + 1)

while chances > 0:
    guess = int(input(f"Enter your guess ({chances} chances left): "))
    if guess == number:
        print("Congratulations! You guessed the number correctly.")
        break
    elif guess < number:
        print("The number is greater than your guess.")
    else:
        print("The number is smaller than your guess.")
    chances -= 1
else:
    print(f"Sorry! You lost the game. The number was {number}.")