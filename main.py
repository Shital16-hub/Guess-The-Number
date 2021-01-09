## Guess The Number ##

from art import logo
from replit import clear
import random


def attempt(difficulty):
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    return attempts


def play_game():
    difficulty = input("Chosse difficulty: Type 'easy' or 'hard'").lower()
    random_no = random.randint(1, 100)
    print(random_no)
    new_attempts = attempt(difficulty) - 1
    is_game_over = False
    while not is_game_over:
        guess = int(input("Make a Guess: "))
        if new_attempts == 0:
            print("Lose.You have exhausted all attempts")
            is_game_over = True

        elif guess > random_no:
            print("Too High")
            new_attempts -= 1
            print(f"You have {new_attempts + 1} attempts remaining to guess the number.")

        elif guess < random_no:
            print("Too Low")
            new_attempts -= 1
            print(f"You have {new_attempts + 1} attempts remaining to guess the number.")

        else:
            print(f"You Guessed Right Number: {random_no}")
            is_game_over = True
    should_play = input("Do you want to play game? Type 'yes' or 'no'").lower()
    if should_play == 'yes':
        clear()
        play_game()

    else:
        print("Thank You")


print(logo)
print("Welcome to Number Guessing Game.\nI am thinking number between 1 and 100.")
play_game()

