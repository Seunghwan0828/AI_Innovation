# 이미지 처리 - Arithmetic 연산
# Image Addition, Image Blending, Image Substraction, Bit Operation

# Image Blending :
#   - 이미지들의 합
#   - 이미지 겹쳐보이게 하거나, 투명하게 보이게 하는 방법
#   y = image1 * (1-특정 가중치) + image2 * 특정가중치 / 특정가중치: 0 ~ 1의 값을 가진다

# substract
# add or addWeighted 처럼 값을 더하는 것이 아니라, 빼는 개념
# 이미지간의 크기가 같아야 합니다.

import cv2

img1 = cv2.imread("paper.jpg")
print(img1.shape)
img2 = cv2.imread("hummingbird.jpg")
img2 = cv2.resize(img2, (640, 426))
print(img2.shape)

# img_blend = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
# cv2.imshow("blended_image", img_blend)

img_sub = cv2.subtract(img1, img2)
cv2.imshow("subtracted_image", img_sub)

cv2.waitKey(0)
cv2.destroyAllWindows()