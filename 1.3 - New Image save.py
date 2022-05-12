import cv2
print("Package Imported")
img = cv2.imread("Dino.png")
# The Width, height and the RGB frames is shown
print("width:{}".format(img.shape[1]))
print("height:{}".format(img.shape[0]))
print("RGB:{}".format(img.shape[2]))

cv2.imshow("Dino", img)
cv2.waitKey(0)
# The image file Dinos is now placed in the program folder. The image is saved.
cv2.imwrite("Dinos.jpg",img)