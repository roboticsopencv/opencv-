##new_img = a * original_img + b

import cv2
import numpy as np

img = cv2.imread("C:/Users/PDR/PycharmProjects/OpenCVProject/practice/resources/wave.png")
img2 = np.zeros(img.shape, img.dtype)
print("ing2",img2)
contrast_img = cv2.addWeighted(img, 2.5, img2, 0, 0)
#cv2.addWeighted(source_img1, alpha1, source_img2, alpha2, beta)
cv2.imshow('Original Image1', img)
cv2.imshow('Original Image2', img2)
cv2.imshow('Contrast Image', contrast_img)

#Blur the image
blur_image = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Blur Image', blur_image)


#Convert image to grayscale (Black & White)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2)

cv2.imshow('Converted Image', gray_img)

cv2.waitKey(0)