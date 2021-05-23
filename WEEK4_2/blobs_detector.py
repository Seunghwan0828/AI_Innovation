import cv2
import numpy as np

image = cv2.imread("someshapes.jpg")
cv2.imshow("original image", image)

# 기본 설정으로 물방울(Blob) detector 초기화
detector = cv2.SimpleBlobDetector_create()

# 이제 찾아라!
find_blobs = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, find_blobs, blank, (255, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(find_blobs)
text = "Total Number of Blobs: " + str(number_of_blobs)
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

cv2.imshow("detect image", blobs)

# 이제부터 세부설정을 가진 detector를 생성
params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.9

params.filterByConvexity = False
params.minConvexity = 0.2

params.filterByInertia = True
params.minInertiaRatio = 0.01

# 세부적인 설정을 추가한 물방울(Blob) detector 
detector = cv2.SimpleBlobDetector_create(params)

# 이제 찾아라!
find_blobs = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, find_blobs, blank, (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("parameter detect image", blobs)


cv2.waitKey(0)
cv2.destroyAllWindows()