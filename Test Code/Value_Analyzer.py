import cv2
import numpy as np

green = np.uint8([[[0,255,0 ]]])

img = np.zeros( (30, 30, 3), np.uint8)
img[:] = (0, 255, 0)

cv2.imshow("Test Screen", img)
cv2.waitKey(0)

hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green )

# Output
# [[[ 60 255 255]]]