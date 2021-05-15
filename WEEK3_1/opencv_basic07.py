import cv2

img = cv2.imread("../WEEK3_2/paper.jpg")
img1 = cv2.imread("../WEEK3_2/color.jpg")

print(img.shape)
print(img.size)
# 817920 = width * height * channel (640 * 426 * 3)
print(img.dtype)

b, g, r = cv2.split(img)
b1, g1, r1 = cv2.split(img1)
img = cv2.merge((b1, g1, b1))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()