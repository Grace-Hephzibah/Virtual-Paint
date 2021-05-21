import cv2
import numpy as np

import MyColors as col
# import My_OpenCV_Functions as mcv

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 10)

def findColor(img, myColors):
    for color in myColors:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(color[1:4])
        upper = np.array(color[4:7])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)

while True:
    success, img = cap.read()
    findColor(img, col.myColors)
    cv2.imshow("Video Console", img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break