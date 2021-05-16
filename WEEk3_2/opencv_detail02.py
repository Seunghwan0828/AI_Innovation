# image filtering
# 이미지에 존재하는 픽셀을 해당하는 픽셀의 주위에 있는 픽셀들을 활용 특정한 함수를 적용한 결과를 기반으로 수정한다라는 개념

# 1. mask를 생성
# 2. 이 mask를 기준으로 주변값들을 연산

# cv2.blur 함수
# cv2.blur(image, destination, kernel-size, [achor type, bordertype])

import cv2

img = cv2.imread("paper.jpg")

img_blur5 = cv2.blur(img, (5, 5))
img_blur9 = cv2.blur(img, (9, 9))

cv2.imshow("Original image", img)
cv2.imshow("blurred image5", img_blur5)
cv2.imshow("blurred image9", img_blur9)
cv2.waitKey(0)
cv2.destroyAllWindows()