import random

# Created by @lets.learn.code -- 01/06/2020

print("Welcome to the guessing game!")
print("--------How it works---------")
print("(1) You only get 10 guesses")
print("(2) Choose a number between 1 and 99")
print("(3) If attempt says low pick a higher number")
print("(4) If attempt says high pick a lower number")

print("\nGood luck!")

# Program selects a random integer between 1 and 99
num = random.randint(1, 99)

guess = int(input("\nEnter an integer from 1 to 99: "))

# We declare nine guesses because one has already been used above.
attempts = 9

# While the guess is not correct and we have attempts left keep looping.
while num != "guess" and attempts > 0:
    if guess < num:
        # Guess is lower than number - Ask user for new input - Decrease attempts by 1
        print("\nGuess is low you have", attempts, "remaining")
        guess = int(input("Enter an integer from 1 to 99: "))
        attempts -= 1
    elif guess > num:
        # Guess is higher than number - Ask user for new input - Decrease attempts by 1
        print("\nGuess is high you have", attempts, "remaining")
        guess = int(input("Enter an integer from 1 to 99: "))
        attempts -= 1
    else:
        # User guesses the number correctly - print msg and break the loop.
        print("\nYou answer is correct!! -- WINNER!")
        break

# If after leaving the loop and our guesses are at zero then we got it incorrect.
if attempts == 0:
    print("\nYou have ran out of guesses... - Better luck next time!")
