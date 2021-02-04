"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730387431"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

cookie_number: int = randint(1,4)

if cookie_number < 2:
    print("Fortune Cookie Message 1")
else:
    if cookie_number < 3:
        print("Fortune Cookie Message 2")
    else:
        if cookie_number < 4:
            print("Fortune Cookie Message 3")
        else:
            print("Fortune Cookie Message 4")

print("Now, go spread positive vibes!")