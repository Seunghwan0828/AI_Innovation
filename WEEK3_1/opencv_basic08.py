import cv2

img1 = cv2.imread("../WEEK3_2/paper.jpg")
img2 = cv2.imread("../WEEK3_2/color.jpg")

print(img1.shape)
print(img2.shape)

# textoftheimage = img[109:331, 94:475]
# img[59:281, 44:425] = textoftheimage

img1 = cv2.resize(img1, (640, 420))
img2 = cv2.resize(img2, (640, 420))

added_img = cv2.addWeighted(img1, .8, img2, .2, 0)

cv2.imshow("image", added_img)
cv2.waitKey(0)
cv2.destroyAllWindows()