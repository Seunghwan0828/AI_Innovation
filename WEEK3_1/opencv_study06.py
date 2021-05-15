import cv2
import numpy as np

image = cv2.imread("./shape.png")
original_image = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 30, 200) # 0~255
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

display_image = np.hstack((original_image, image))

cv2.imshow("Image", display_image)
cv2.waitKey(0)