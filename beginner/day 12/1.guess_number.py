import art
import random
comp_guess=random.randint(0,101)
print(art.logo)
print("Welcome to the Number Guessing Game! ")
print(f"I'm thinking of a number between 1 and 100. the guess is {comp_guess}")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard: ")


def level(difficulty):
    ''' this function get the level of the player and return the number of attempts to win the game'''
    if difficulty == 'easy':
        attempts = 10
        return attempts
    elif difficulty == 'hard':
        attempts = 5
        return attempts
attempts=level(difficulty)

while attempts>0:
    print(f"you have {attempts} remainig to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess != comp_guess:
        attempts-=1
        if user_guess > comp_guess:
            print("Too high.")
            print("guess again. ")
        else:
            print("Too low")
            print("guess again.")
    if user_guess==comp_guess:
        print("you are wright")
        attempts=0
