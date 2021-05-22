# Image THresholding
# 1. 시각적 데이터를 단순화 
# 2. 이미지 세그멘테이션 가능하게 해준다 (image segmentation)
# 이미지를 구성하는 픽셀에 2가지 수준을 할당한다라는 개념
# 할당은 특정한 threshold 값을 기준으로 합니다.
# above & below
# 픽셀의 값이 thesshold보다 높으면 white 을 할당
# 픽셀의 값이 threshold보다 낮으면 black 을 할당

import cv2

img = cv2.imread("hummingbird.jpg")
print(img.shape)
img = cv2.pyrDown(img)
print(img.shape)

# cv2.imshow("image thresholding", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image gray thresholding", img_gray)

# simple image thresholding
ret, simple_thresholding1 = cv2.threshold(img_gray, 80, 250, cv2.THRESH_BINARY)
ret, simple_thresholding2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)

# CV2.THRESH_BINARY : 픽셀의 값이 threshold 보다 크면 최대값을 할당 아니면 0을 할당
# CV2.THRESH_BINARY_INV : 픽셀의 값이 threshold 보다 크면 0으로 할당
# CV2.THRESH_TRUNC : 픽셀의 값이 threshold 보다 크면 값을 버림
# CV2.THRESH_TOZERO : 픽셀의 값이 threshold 보다 낮으면 0으로 할당
# CV2.THRESH_TOZERO_INV : 픽셀의 값이 threshold 보다 낮으면 1으로 할당

cv2.imshow("image gray thresholding1",  simple_thresholding1)
# cv2.imshow("image gray thresholding2",  simple_thresholding2)

cv2.waitKey(0)
cv2.destroyAllWindows()