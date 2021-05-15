import cv2

image = cv2.imread("../WEEK3_2/color.jpg")

print(image.shape)

cv2.imshow("Image Show",image)
cv2.waitKey(0)  # 0은 무기한 대기를 의미합니다. 나머지 숫자는 기다리는 초 * 1000 (원래 단위 ms)