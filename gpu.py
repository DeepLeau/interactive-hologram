import cv2
import mediapipe as mp
import pyautogui
import math
import tensorflow as tf
import time

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
