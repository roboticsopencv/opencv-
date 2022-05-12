# EROSION DILATION - COLOUR IMAGE

# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

# Reading the input image
img = cv2.imread('C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic19.webp',1)

# Taking a matrix of size 5 as the kernel
kernel1 = np.ones((1, 1), np.uint8)
kernel2 = np.ones((5, 5), np.uint8)
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
#canny = cv2.Canny(img, 50, 100)
#img_erosion = cv2.erode(canny, kernel1, iterations=3)
#img_dilation = cv2.dilate(canny, kernel2, iterations=1)
img_erosion = cv2.erode(img, kernel1, iterations=10)
img_dilation = cv2.dilate(img, kernel2, iterations=1)

cv2.imshow('Original', img)
#cv2.imshow('Canyy Edges', canny)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)