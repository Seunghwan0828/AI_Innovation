# log transforamtion
# 이미지를 개선할 때 사용
# gray 수준 변환중 하나
# 모든 픽셀의 값을 로그 값으로 변경시켜준다.
# 이미지의 어두운 색을 가진 픽셀을 밝게 해준다
# 일반적으로 어두운 게열의 이미지에 적용
# 공식 : result = c * log(1 + r)
# result = 픽셀의 계산값
# r = 입력 픽셀 값
# c = scaling (증폭, 확장)시킬 값
# c = 255 / (log(1 + 입력한 픽셀값중 최대값))

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

c = 255 / np.log(1 + np.max(img))
log = c * (np.log(img + 1))

img_log = np.array(log, dtype=np.uint8)

cv2.imshow("Original", img)
cv2.imshow("log Image", img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()
