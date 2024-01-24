import cv2
import mediapipe as mp
import pyautogui
import math
import tensorflow as tf
import time
import audioop
from math import log10
import pyaudio

p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = 3
alpha = 0.5  # Facteur de lissage (entre 0 et 1)
rms = 1

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH)
    
    rms = (1 - alpha) * rms + alpha * rms
    
    db = 20 * log10(rms)

# Variables à déterminer

    # Variables claquement de doigts
    seuil_micro_min = 70
    seuil_micro_max = 90
    x_micro,y_micro = 50,50
    
    # Variables souffle sur la caméra
    seuil_souffle = 120
    x_camera, y_camera = 50,50
    
    if db > seuil_micro_min and db < seuil_micro_max:
        pyautogui.moveTo(x_micro, y_micro)
        pyautogui.click()
    
    elif db > seuil_souffle :
        pyautogui.moveTo(x_camera,y_camera)
        pyautogui.click()
    print(f"Décibels: {db}")
    
    return in_data, pyaudio.paContinue

stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

# Configurer l'utilisation du GPU par TensorFlow
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Initialiser MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

pyautogui.FAILSAFE = False

while True:
    success, image = cap.read()

    h,w,c = image.shape
    largeur = 1920
    hauteur = 1080

    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            fingers_tip_points = [handLms.landmark[4], handLms.landmark[8], handLms.landmark[12],
                                  handLms.landmark[16], handLms.landmark[20]]

            palm_base = handLms.landmark[0]
            palm_base_x, palm_base_y = int(palm_base.x * image.shape[1]*largeur/w), int(palm_base.y * image.shape[0]*hauteur/h)
            
            finger_4_x, finger_4_y, finger_8_x, finger_8_y = int(fingers_tip_points[0].x * image.shape[1]*largeur/w), int(fingers_tip_points[0].y * image.shape[0]*hauteur/h), int(fingers_tip_points[1].x * image.shape[1]*largeur/w), int(fingers_tip_points[1].y * image.shape[0]*hauteur/h)

            x = (finger_4_x + finger_8_x)/2
            y = (finger_4_y + finger_8_y)/2

            pyautogui.moveTo(x, y,_pause = False)

            for tip_point in fingers_tip_points:
                tip_point_x, tip_point_y = int(tip_point.x * image.shape[1]*largeur/w), int(tip_point.y * image.shape[0]*hauteur/h)
                cv2.line(image, (palm_base_x, palm_base_y), (tip_point_x, tip_point_y), (255, 0, 0), 2)

            
            
            distance = math.sqrt((finger_4_x - finger_8_x)**2+(finger_4_y - finger_8_y)**2)        
            seuil = 40

            # putting the FPS count on the frame 
            cv2.putText(image, str(distance), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  

            if distance < seuil:
                print("Clic")
                cv2.putText(image, "Left Click", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                pyautogui.click() ##_pause=False
                time.sleep(0.01)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", image)
    cv2.waitKey(1)
    
p.terminate()
