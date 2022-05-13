# ROTATE PICTURE

import cv2
img = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic4.jpg")
height, width = img.shape[0:2]
print(height,width)
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)

#Cropping the image
startRow = int(height*.50)
print(startRow)
startCol = int(width*.20)
print(startCol)
endRow = int(height*.80)
endCol = int(width*.55)
print(endRow)
print(endCol)

croppedImage = img[startRow:endRow, startCol:endCol]
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(0)