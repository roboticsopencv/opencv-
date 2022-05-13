# IMAGE ADDITION
import cv2

image1 = cv2.imread("C:/Users/anju/Desktop/1.jpg",1)
image2 = cv2.imread("C:/Users/anju/Desktop/2.jpg")

img = cv2.add(image1, image2)

cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Added Image', img)
cv2.waitKey(0)