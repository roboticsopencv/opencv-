import cv2
print("Package Imported")
# Reading an image from the folder
img = cv2.imread("Dino.png")
# Displaying the image
cv2.imshow("Dino", img)
# Holding the Image on screen until any button is pressed (0)
cv2.waitKey(0)