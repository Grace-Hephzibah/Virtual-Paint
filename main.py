import cv2
import numpy as np

myColors = [
    ["YELLOW", 14, 137, 174, 140, 235, 255],
    ["GREEN", 48, 95, 48, 83, 182, 140],
    ["BLUE", 100, 171, 74, 122, 240,255],
    ["RED", 168, 172, 120, 179, 235, 192]
]

myColorsValues = [[0, 255, 255], [0, 255, 0], [255, 0, 0], [0, 0, 255]]

myPoints = [] ##[x, y, colorID]

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 10)

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[1:4])
        upper = np.array(color[4:7])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        #cv2.imshow("Mask" + color[0], mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints

def getContours(img):
    x, y, w, h = 0, 0, 0, 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for points in myPoints:
        cv2.circle(imgResult, (points[0], points[1]), 10, myColorValues[points[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorsValues)

    if len(newPoints)!= 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!= 0:
        drawOnCanvas(myPoints, myColorsValues)

    cv2.imshow("Video Console", imgResult)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break