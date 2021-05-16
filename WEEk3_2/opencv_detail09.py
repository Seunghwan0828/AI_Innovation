import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

mat1 = np.float32([[50, 50], [200, 50], [50, 200]]) # 이미지의 현재 3개의 점
mat2 = np.float32([[10, 100], [200, 50], [100, 250]]) # 이미지에 지정한 3개의 점으로 이동하려 한다

aff_matrix = cv2.getAffineTransform(mat1, mat2)
aff_img = cv2.warpAffine(img, aff_matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("aff Image", aff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()