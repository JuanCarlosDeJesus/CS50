"""
implement a program that:

Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.

"""
import random
import sys


while True:
    try:
        lvl = int(input("Level: ").strip())
        if lvl > 1:
            break
    except:
        pass

n = random.randint(1,lvl)
# print(n)

while True:
    try:
        g = int(input("Guess: ").strip())
        if g > 0:
            if g > n:
                print("Too large!")
            elif g < n:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass