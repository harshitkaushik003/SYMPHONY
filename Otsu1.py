import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.VideoCapture(0)
while True:
        success, frame = image1.read()
        original = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        thresh2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.ADAPTIVE_THRESH_MEAN_C)[1]
        cv2.imshow("OTSU", thresh1)
        cv2.imshow("ADAPTIVE MEAN", thresh2)
        cv2.waitKey(1)

cv2.destroyAllWindows()
