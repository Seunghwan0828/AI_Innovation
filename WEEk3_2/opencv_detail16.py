# ROT
# in Computer Vision : Region of Interest
# in Economics : Return of Invesrment

import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

roi = cv2.selectROI(img)

print(roi)
crop = img[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

cv2.imshow("roi Image", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()