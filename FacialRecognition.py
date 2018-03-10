#python3

import numpy as np
import cv2
import time


frames = 30

cap = cv2.VideoCapture(0)
cap.open(0)

def capturingPicture():
    retval, image = cap.retrieve()
    return image

counter = 0

while counter < frames:
    cap.read()
    counter = counter + 1

cv2.imwrite("practice.png",capturingPicture())