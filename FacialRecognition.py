from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import numpy as np
import cv2
import time
from skimage.measure import compare_ssim as diffPixels
import sys
import config



frames = 30

cap = cv2.VideoCapture(0)
cap.open(0)

surroundingsChanged = True

def capturingPicture():
    output, image = cap.retrieve()
    return image
repeat = ""

def findSum(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            sum += arr[i][j]
    return sum

def comparingPictures(img1, img2):
    grayScale1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grayScale2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    pixelVal1 = np.sum(grayScale1)
    pixelVal2 = np.sum(grayScale2)

    change = pixelVal2 - pixelVal1
    if (change > (pixelVal1 * 0.3)):
        return True
    return False

cv2.imwrite("practice.png",capturingPicture())

while (repeat == ""):
    counter = 0
    while counter < frames:
        cap.read()
        counter = counter + 1

    img2 = capturingPicture()
    img1 = cv2.imread("practice.png")

    if (comparingPictures(img1, img2)):
        cv2.imwrite("practice.png", img2)
        surroundingsChanged = True

    if (surroundingsChanged):
        app = ClarifaiApp(api_key = config.key)
        model = app.models.get('face-v1.3')

        image = ClImage(file_obj=open('practice.png', 'rb'))
        response = model.predict([image])

        val = response["outputs"][0]["data"]
        if (val == {}):
            print("There is not a person waiting in front of the camera")
            f = open('output.txt', 'w').close()
        else:
            print("Showing Image of Person")
            person  = cv2.imread("practice.png")
            f = open('output.txt', 'w')
            f.write("A person is waiting in front of the camera")
            f.close()
    #        cv2.imshow("image", person)
    #        cv2.waitKey(0)
    surroundingsChanged = False
    time.sleep(5)