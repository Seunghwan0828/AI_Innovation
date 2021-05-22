import cv2
import numpy as np

img = cv2.imread("sudoku.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize= 3)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=200, maxLineGap=30) # Hough 변환 : 선과 관련된 곳에 많이 사용

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)

cv2.imshow("Image by Hough", img)
cv2.waitKey(0)
cv2.destroyAllWindows()