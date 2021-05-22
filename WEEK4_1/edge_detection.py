# Edge (모서리)
# 1. 이미지에서 갑자기 끊겨지는 변화
# 2. 이미지에서 갑자기 과도하게 변경되는 부분
# 3. 서로 다른 segmentation와 같은 부분

# Edge Detection을 왜 할까?
# 1. 모양의 정보를 얻고자 한다.
# 2. Feature extration (특성 추출)
# 3. 패턴 인식
# 4. 이미지 형태 변형

# Edge Detection을 하는 방법
# 1. Sobel
# 2. Prewitt
# 3. Laplacian
# 4. Canny

# Canny Edge Detection
# 1. 가장 효과적이고 복잡한 방법
# 2. 과정
#   1) 필터를 통해서 smooth 노이지를 제거하거나 매끈하게 만들어준다. --gaussian filter
#   2) gradient 연산을 통해서 gradient를 계산
#   3) edge point 모서리 지점 추출
#   4) edge point들을 연결


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    ret, frame = cap.read()

    cv2.imshow("Video Show", frame)

    img_edge1 = cv2.Canny(frame, 10, 100)
    img_edge2 = cv2.Canny(frame, 50, 150)
    img_edge3 = cv2.Canny(frame, 100, 200)
    cv2.imshow("Canny Show1", img_edge1)
    cv2.imshow("Canny Show2", img_edge2)
    cv2.imshow("Canny Show3", img_edge3)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break