import numpy as np
import cv2

cap = cv2.VideoCapture("slow_traffic_small.mp4")

while(1):
    ret, img = cap.read()

    roi = img[200:250, 300:400]

    if ret == True:
        cv2.imshow("traffic video",img)

        key_value = cv2.waitKey(30) & 0xFF
        if key_value == 27: #Enter ESC Key
            break
        else:
            break