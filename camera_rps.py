# %%

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

class RockPaperScissor():

    def __init__(self):
        self.model = load_model('keras_model.h5', compile=False)
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.labels = ["Rock","Paper","Scissors","Nothing"]
        self.time_limit = 3 # Seconds
        
        

    def get_computer_choice(self):

        computer_choice = random.choice(["Rock","Paper","Scissors"])

        return computer_choice
            


    def get_prediction(self):

        Countdown = False

        start = time.time()

        time_limit = self.time_limit
        
        while True:

            ret, self.frame = self.cap.read()

            if Countdown == True:

                current = time.time()

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(self.frame,str(time_limit),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)
                
                if current - start >= 1:
                    start = current
                    time_limit = time_limit - 1

            if time_limit <= 0:

                prediction = self.model.predict(self.data, verbose = 0 )
                prediction2 = self.labels[np.argmax(prediction)]
                user_choice = prediction2
                print(prediction2)
                break

            if ret==True:
                resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                self.data[0] = normalized_image

            cv2.imshow('frame',self.frame)
            # cv2.startWindowThread()
            if cv2.waitKey(1) & 0xFF == ord('c'):
                Countdown = True

        return user_choice

    

    def get_winner(self):
    
        computer_wins = 0
        user_wins = 0

        while True:

            computer_choice = "Paper"

            user_choice = self.get_prediction()

            if user_choice == "Nothing":
                print("Try again!")

            elif user_choice == computer_choice:
                print("It is a tie!")

            elif user_choice == 'Rock' and computer_choice == 'Scissors':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("User wins:", user_wins ," / Computer wins:", computer_wins)

            elif user_choice == 'Scissors' and computer_choice == 'Paper':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("User wins:", user_wins ," / Computer wins:", computer_wins)

            elif user_choice == 'Paper' and computer_choice == 'Rock':
                print("User won 1 point!")
                user_wins = user_wins + 1
                print("User wins:", user_wins ," / Computer wins:", computer_wins)

            else:
                print("Computer won 1 point!")
                computer_wins = computer_wins + 1
                print("User wins:", user_wins ," / Computer wins:", computer_wins)
        
            if user_wins == 3 or computer_wins == 3:
                break

        
        if user_wins == 3:
            print("You won!")
        else: 
            print("You lost!")

    
        self.cap.release()
        cv2.imshow('frame', self.frame)
        cv2.destroyWindow('frame')
        cv2.waitKey(1)



rps = RockPaperScissor()
rps.get_winner()




# %%
