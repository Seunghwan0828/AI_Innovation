# bit 연산 : extraction
#   - masking에 큰 도움
#   - AND, OR, XOR, NOT을 사용한다.

import cv2

img1 = cv2.imread("paper.jpg")
print(img1.shape)
img2 = cv2.imread("hummingbird.jpg")
img2 = cv2.resize(img2, (640, 426))
print(img2.shape)

# bit_and = cv2.bitwise_and(img1, img2)
# cv2.imshow("bit_and_image", bit_and)

# bit_or = cv2.bitwise_or(img1, img2)
# cv2.imshow("bit_and_image", bit_or)

# bit_xor = cv2.bitwise_xor(img1, img2)
# cv2.imshow("bit_and_image", bit_xor)

bit_not = cv2.bitwise_not(img1, img2)
cv2.imshow("bit_and_image", bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()