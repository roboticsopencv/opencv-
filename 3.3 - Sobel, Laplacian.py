# SOBEL AND LAPLACIAN FILTER

import cv2
import numpy as np

# read image
image = cv2.imread('C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic14.jpg')
cv2.imshow("Original", image)

#laplacian gradient
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Converted to Gray", image1)
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

#Sobel gradient representation
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)