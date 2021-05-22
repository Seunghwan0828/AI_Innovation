import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255 #(255, ) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


cap = cv2.VideoCapture(0)

while(1):
    ret, image = cap.read()
    # image = cv2.imread("road3.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
        (0, height),
        # (width / 2, height /2),
        (width / 2, height / 3),
        (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 200, 250)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image, rho = 10, theta = np.pi/180, threshold=150, lines=np.array([]), minLineLength=100, maxLineGap=25)

    def draw_the_lines(img, lines):
        img = np.copy(img)
        blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (255, 255, 0), 3)
        img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)

        return img

    def draw_the_lines2(img, lines):
        img = np.copy(img)
        blank_image = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (255, 255, ), 3)

        return img

    image_with_lines = draw_the_lines(image, lines)
    image_with_lines2 = draw_the_lines2(cropped_image, lines)

    # canny_image_crop = cv2.Canny(cropped_image, 100, 200)

    # plt.imshow(cropped_image)
    # plt.show()

    cv2.imshow("lined image", image_with_lines)
    # cv2.imshow("lined image2", image_with_lines2)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break