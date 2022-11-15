import random

def get_computer_choice():

    computer_choice = random.choice(["Rock", "Paper","Scissors"])

    return computer_choice

def get_user_choice():

    user_choice = input("Enter your choice: ")

    return user_choice