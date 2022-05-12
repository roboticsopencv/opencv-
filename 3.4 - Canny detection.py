# CANNY DETECTION

import cv2
import numpy as np

# read image
image = cv2.imread('C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic14.jpg')
cv2.imshow("Original", image)
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image1)
print(image1)

canny = cv2.Canny(image1, 35, 170)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
