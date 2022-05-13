# COLOUR DETECTION - GREEN COLOUR

import cv2
import numpy as np

img = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic3.jfif")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)
lower_green = np.array([34, 177, 76])
upper_green = np.array([255, 255, 255])

masking = cv2.inRange(hsv_img, lower_green, upper_green)

cv2.imshow("Original Image", img)
cv2.imshow("Green Color detection", masking)
cv2.waitKey(0)