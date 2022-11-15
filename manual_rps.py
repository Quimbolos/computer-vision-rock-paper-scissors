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
        if user_choice == 'Rock' & computer_choice == 'Scissors':
            print("You won!")
        elif user_choice == 'Scissors' & computer_choice == 'Paper':
            print("You won!")
        elif user_choice == 'Paper' & computer_choice == 'Rock':
            print("You won!")
        else:
            print("You lost")

    print(user_choice,computer_choice)

get_winner()
# %%
