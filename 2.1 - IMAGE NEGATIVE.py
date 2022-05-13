# IMAGE NEGATIVE

import cv2
import numpy as np
# Load the image
img = cv2.imread("pic1.jfif")
# Check the datatype of the image
print(img.dtype)
print(img)
# Subtract the img from max value(calculated from d type)
# s = T(r) = L – 1 – r
img_neg = 255 - img
# Show the image
cv2.imshow('Original',img)
cv2.imshow('negative',img_neg)
cv2.waitKey(0)