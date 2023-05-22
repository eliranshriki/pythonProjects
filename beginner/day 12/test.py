import art
import random
EASY_LEVEL=10
HARD_LEVEL=5
comp_guess = random.randint(1, 100)
print(art.logo)
print("Welcome to the Number Guessing Game! ")
print(f"I'm thinking of a number between 1 and 100. the guess is {comp_guess}")


def level():
    ''' this function get the level of the player and return the number of attempts to win the game'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == 'easy':
        return EASY_LEVEL
    elif difficulty == 'hard':
        return HARD_LEVEL


def check (user_guess,comp_guess):
    """this function check if the user is guess the number or not"""
    if user_guess != comp_guess:
        if user_guess > comp_guess:
            print("Too high.")
            print("guess again. ")
        else:
            print("Too low")
            print("guess again.")
    if user_guess==comp_guess:
        print(f"You got it! the answer was {comp_guess}")


def game(attempts):
    print(f"you have {attempts} remainig to guess the number.")
    user_guess = int(input("Make a guess: "))
    return user_guess



turns=level()
print(f"you have {turns} remaining to guess the number.")
user_guess = int(input("Make a guess: "))
check(user_guess,comp_guess)