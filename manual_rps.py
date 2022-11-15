# %%

import random

def get_computer_choice():

    computer_choice = random.choice(["Rock", "Paper","Scissors"])

    return computer_choice

def get_user_choice():

    user_choice = input("Enter your choice: ")

    return user_choice

def get_winner(user_choice = get_user_choice(),computer_choice = get_computer_choice()):

    if user_choice == computer_choice:
        print("It is a tie!")

    else:
        if user_choice == 'Rock' and computer_choice == 'Scissors':
            print("You won!")
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            print("You won!")
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            print("You won!")
        else:
            print("You lost")

def play():

    return get_winner()

play()
# %%
