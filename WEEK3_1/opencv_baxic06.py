import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolrImage = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        mycolrImage[:] = [blue, green, red]

        cv2.imshow("color", mycolrImage)

img = cv2.imread("../WEEK3_2/paper.jpg")
cv2.imshow("image", img)

points = []
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()