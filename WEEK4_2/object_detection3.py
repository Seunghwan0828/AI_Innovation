import cv2
import time
import numpy as np

car_classifier = cv2.CascadeClassifier("haarcascade_car.xml")

cap = cv2.VideoCapture("cars.avi")

while cap.isOpened():
    time.sleep(0.05)

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cars = car_classifier.detectMultiScale(gray, 1.4, 2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow("cars",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()