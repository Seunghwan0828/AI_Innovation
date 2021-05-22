# Blur : 이미지를 단순화 하면서도 노이즈 제거 역할
# noise : 이미지에 존재하는 원래의 예상하는 픽셀의 값이 아닌 밝기나 색의 변종 
# 이미지의 노이즈! 생길 수밖에 없다! 이유는?
# 1. 이미지라는 것은 전기적으로 전송! 디지털카메라로 사진을 찍고, 네트워크를 통해서 전송 ...
# 2. 센서의 문제가 생기거나 조정이 일어났을 때
# 3. 빛의 강도 ISO Factor

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
print(img.shape)
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

kernel = np.ones((5, 5), np.uint8)
print(kernel.shape)
print(kernel)

# erosion technique
img_err = cv2.erode(img, kernel, iterations = 5)

# dilation technique
img_dil = cv2.dilate(img, kernel, iterations = 5)

# morphological opening technique
img_opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# morphological closing technique
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# cv2.MORPH_GRADIENT
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# cv2.MORPH_TOPHAT
img_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# cv2.MORPH_BLACKHAT
img_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("original image", img)
# cv2.imshow("erosion image", img_err)
# cv2.imshow("dilation image", img_dil)
cv2.imshow("morph open image", img_opn)
cv2.imshow("morph close image", img_close)
cv2.imshow("morph gradient image", img_gradient)
cv2.imshow("morph tophat image", img_tophat)
cv2.imshow("morph blackhat image", img_blackhat)


cv2.waitKey(0)
cv2.destroyAllWindows()