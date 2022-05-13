# IMAGE SUBTRACTION
import cv2

image1 = cv2.imread("C:/Users/Desktop/19R207/pic3.jpg",1)
image2 = cv2.imread("C:/Users/Desktop/19R207/pic4.jpg")

img = cv2.subtract(image1, image2)

cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Subtracted Image', img)
cv2.waitKey(0)