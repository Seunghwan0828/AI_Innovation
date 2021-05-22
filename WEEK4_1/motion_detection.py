import cv2
import numpy as np

cap = cv2.VideoCapture(0)

corner_detection_param = dict(maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
lucas_kanade_param = dict(winSize=(15, 15), maxLevel=2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
colors = np.random.randint(0, 255, (100, 3))

while (1):
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    p0 = cv2.goodFeaturesToTrack(frame_gray, mask=None, **corner_detection_param)
    mask = np.zeros_like(frame)

    p1, st, err = cv2.calcOpticalFlowPyrLK(frame_gray, frame_gray, p0, None, **lucas_kanade_param)

    good_new = p1[st == 1]
    good_old = p0[st == 1]
    
    cv2.imshow("Show Window", p0)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break