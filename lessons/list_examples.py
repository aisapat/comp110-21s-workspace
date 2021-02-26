"""Some examples of lists."""

rolls: list[int]

rolls = [2, 3, 2, 6]   # Declare a variable whose type is list of ints

print(f"Length of rolls is {len(rolls)}")   #Initialize w/ list literal sytax
print(f"The last item of the list is {rolls[len(rolls) -1]}")

from random import randint
rolls.append(randint(1,6))  # List's append method adds to the end of a list
print(rolls)

rolls.pop()   # List's pop method, with no arguement, removes the last item of the list
rolls.pop(0)    #List's pop method, with one arguement, pops a specific index
print(rolls)


words: list[str] = list()   #Construct an empty list ususing a list constructor
words.append("Hello")
print(words)

