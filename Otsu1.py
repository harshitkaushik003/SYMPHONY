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






# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#
# # applying Otsu thresholding
# # as an extra flag in binary
# # thresholding
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
#                              cv2.THRESH_OTSU)
#
# # the window showing output image
# # with the corresponding thresholding
# # techniques applied to the input image
# cv2.imshow('Otsu Threshold', thresh1)
#
# # De-allocate any associated memory usage
# if cv2.waitKey(0) & 0xff == 32:
#     cv2.destroyAllWindows()