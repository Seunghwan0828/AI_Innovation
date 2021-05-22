import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

img_laplacian = cv2.Laplacian(img, cv2.CV_16U)
cv2.imshow("origianl image", img)
cv2.imshow("laplacian image", img_laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()