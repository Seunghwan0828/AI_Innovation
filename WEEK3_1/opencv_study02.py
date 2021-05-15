import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.circle(img, (100, 100), 50, (0, 255, 0), 10)
cv2.rectangle(img, (200, 200), (400, 400), (0, 0, 255), 1)
cv2.line(img, (160, 160), (359, 29), (255, 0, 0), 5)
cv2.putText(img, "OpenCV", (280, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

cv2.imshow("My Figure", img)
cv2.waitKey(0)