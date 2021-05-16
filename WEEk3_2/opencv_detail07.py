# image rotation = rotation transformation
# 이미지의 축을 변경
# 변경할 각도를 지정해줘야 한다.
# transformation matrix M = [[cos - sin] [sin - cos]]
# OpenCV는 scaled rotation

import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 15, 0.75)

img_rotation = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Rotated Image", img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()