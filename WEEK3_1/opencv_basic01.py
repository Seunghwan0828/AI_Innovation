import cv2

img = cv2.imread("../WEEK3_2/paper.jpg", 0)

# IMREAD_FLAS
# cv2.IMREAD_COLOR : 1 컬러 이미지로 불러오기
# cv2.IMREAD_GRAYSCALE : 0 grayscale로 이미지 불러오기
# cv2.IMREAD_UNCHANGED : -1 : alpha channel 유지하면서 이미지 불러오기 (투명도 유지)

cv2.imshow("image", img)
key_value = cv2.waitKey(0) & 0XFF

if key_value == 27: # 27=ESC(ASCII)
    cv2.destroyAllWindows()
elif key_value == ord('s'):
    print(ord('s'))
    cv2.imwrite("output_paper.png", img)