# %% 
import cv2
from keras.models import load_model
import numpy as np
import random
import time

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

        elif time_limit == 0:

            prediction = model.predict(data)
            prediction2 = labels[np.argmax(prediction)]
            user_choice = prediction2
            cv2.imshow('frame', frame)
            print(prediction2)

        # Press q to close the window
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    return user_choice

def get_winner(user_choice = get_prediction(),computer_choice = get_computer_choice()):

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


get_winner()

# %%

# %%
