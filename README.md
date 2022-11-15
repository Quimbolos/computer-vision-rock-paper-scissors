# Computer Vision RPS

> AiCore computer vision project - end goal: create a Rock-Paper-Scissors game.

## Milestone 1: Set up the environment

Create a new GitHub repo to upload the code and allow version control throughout the project.

## Milestone 2: Create the computer vision system

Create a computer vision model through Teachable Machine with four classes: Rock, Paper, Scissors, and Nothing. Using Teachable Machine, image samples of the 4 different classes are recorded, and the model is trained. The more samples, the more accurate the model will be. Finally, the model is downloaded and added to the GitHub repo.

## Milestone 3: Install the dependencies

Install all the libraries required to run the model. A new conda environment is created, including the following libraries: pip, opencv-python, tensorflow, and ipykernel. Finally, a requirements.txt file is created, and a downloaded script is run to check the model is working as expected.

## Milestone 4: Create a Rock-Paper-Scissors game

Create a Python script that simulates a Rock-Paper-Scissors game. Initially, two functions are defined to store the user's and the computer's choices. Secondly, a third function - get_winner() - is created to choose a winner based on the classic rules of Rock-Paper-Scissors. Finally, a fourth function - play() - is created to call the previous functions and play the games only using this function. For each TASK, changes in the code are committed and pushed to the GitHub repo.

```python

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


```

