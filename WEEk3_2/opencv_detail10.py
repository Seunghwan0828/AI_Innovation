import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

mat1 = np.float32([[110, 600], [200, 500], [300, 250], [500, 400]])
mat2 = np.float32([[200, 200], [200, 250], [400, 0], [650, 500]])

perspective_matrix = cv2.getPerspectiveTransform(mat1, mat2)
print(perspective_matrix)

perspective_image = cv2.warpPerspective(img, perspective_matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Perspective Image", perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
