import cv2
import numpy as np

img = cv2.imread("gray.jpg",0)
ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Gray Image", img)
cv2.waitKey(0)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)