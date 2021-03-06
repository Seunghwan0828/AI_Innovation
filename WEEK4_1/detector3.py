import cv2
import numpy as np

img = cv2.imread("sudoku.jpeg")

cv2.imshow("sudoku", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

img [dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow("corner detect", img)

cv2.waitKey()
cv2.destroyAllWindows()