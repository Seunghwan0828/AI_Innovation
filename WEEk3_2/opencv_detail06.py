# image translation
# 이미지의 객체나 이미지 위치를 옮길때 사용
# 올기는 방향은 (x, y) 방향이다! -> 옮겨진 장소 (tx, ty)

# transformaiton matrix M = [[1 0 tx] [0 1 ty]]

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
print(img.shape)
height, width, _ = img.shape
print(height, width)

flt_var = np.float32([[1, 0, 200], [0, 1, 100]])
# flt_var = np.float32([[1, 0, -200], [0, 1, -100]])
print(flt_var)

img_trans = cv2.warpAffine(img, flt_var, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Translated Image", img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()