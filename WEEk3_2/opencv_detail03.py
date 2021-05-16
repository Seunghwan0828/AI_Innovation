# 피라미드 기법 (pyramid)
# Level 0 : Original Size
# Level 1 : up의 경우 x2 / down의 경우 1/2
# 피라미드 up
#   -원래 이미지의 크기를 2배 늘린다
#   -이미지를 샘플링을 크게하고 blur 처리
# 피라미드 down
#   -원래 이미지의 크기를 1/2 줄다
#   -이미지를 샘플링을 작게하고 blur 처리

# 피라미드 연산의 장점
# 1. 낮은 해상도
# 2. 다양한 이미지의 크기를 얻을수있다
# 3. 쉽게 이미지 처리를 함
# 4. edge를 쉽게 찾을 수 있다.

import cv2

img = cv2.imread("paper.jpg")
print(img.shape)

# img = cv2.pyrUp(img)
# cv2.imshow("pytUp1",img)
# print(img.shape)
# img = cv2.pyrUp(img)
# cv2.imshow("pytUp2",img)
# print(img.shape)

img = cv2.pyrDown(img)
cv2.imshow("pytDown1",img)
print(img.shape)
img = cv2.pyrDown(img)
cv2.imshow("pytDown2",img)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()