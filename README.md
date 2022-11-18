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

def get_winner(computer_choice, user_choice):
    
    if computer_choice == user_choice:
        print('It is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        print('You won!')
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print('You won!')
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print('You won!')
    else:
        print('You lost')


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()


```

## Milestone 5: Use the camera to play Rock-Paper-Scissors

Create a Python script that simulates a Rock-Paper-Scissors game using computer vision. Initially, the hard-coded user guess is replaced with the output of the computer vision model. A new function called get_prediction is created, where the output from the model is converted into a "Rock" / "Paper" / "Scissors" output.
Secondly, a countdown is added to the code using the time.time() function.
Thirdly, another function is created to repeat the game until either the computer or the user wins. For each TASK, changes in the code are committed and pushed to the GitHub repo.


```python

import cv2
import tensorflow as tf
from keras.models import load_model
import numpy as np
import random
import time
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def get_computer_choice():

    computer_choice = random.choice(["Rock","Paper","Scissors"])

    return computer_choice

def get_prediction():

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True:
        start = time.time()
        time_limit = 3 # seconds

        while time_limit > 0:
            
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            labels = ["Rock","Paper","Scissors","Nothing"]

            current = time.time()

            if current - start >= 1:
                start = current
                time_limit = time_limit - 1
        
        else:
            prediction = model.predict(data, verbose = 0 )
            prediction2 = labels[np.argmax(prediction)]
            user_choice = prediction2
            cv2.imshow('frame', frame)
            print(prediction2)
            break
        
    return user_choice

def get_winner(computer_choice = get_computer_choice()):
    
    computer_wins = 0
    user_wins = 0

    while True:

        user_choice = get_prediction()

        if user_choice == "Nothing":
            print("Try again!")

        elif user_choice == computer_choice:
            print("It is a tie!")

        else:
            if user_choice == 'Rock' and computer_choice == 'Scissors':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("user wins are", user_wins)

            elif user_choice == 'Scissors' and computer_choice == 'Paper':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("user wins are", user_wins)

            elif user_choice == 'Paper' and computer_choice == 'Rock':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("user wins are", user_wins)

            else:
                print("Computer won 1 point!")
                computer_wins = computer_wins + 1
                print("Computer wins are", computer_wins)
        
        if user_wins == 3 or computer_wins == 3:
            break

    
    if user_wins == 3:
        print("You won!")
    else: 
        print("You lost!")


get_winner()


```
