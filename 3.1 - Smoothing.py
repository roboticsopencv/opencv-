#SMOOTHING

import cv2
import numpy
# read image
src = cv2.imread('C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic13.jfif')
cv2.imshow("Original", src)

# apply Averaging on src image
blurred = cv2.blur(src, (3, 4))
cv2.imshow("Averaged", blurred)

# apply Median blur on src image
median_blur = cv2.medianBlur(src, 5)
cv2.imshow("Median_Blurred", median_blur)

# apply guassian blur on src image
gaussian_blur = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)

# display input and output image
cv2.imshow("Gaussian Blurred", gaussian_blur)

# apply bilateral filter
bilateral_blur = cv2.bilateralFilter(src, 7, 21, 21)
cv2.imshow("Bilateral Blurred", bilateral_blur)

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image