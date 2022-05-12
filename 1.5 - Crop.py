import cv2
print("Package Imported")
image = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/Dino1.jfif")
# Display Original Image
cv2.imshow("Original", image)
# Crop the Image
corner = image[10:70, 50:140]
cv2.imshow("Cropped", corner)
# Save the Cropped Image
cv2.imwrite("DinoFace.jpg", corner)
# Show the Image after cropping
image[10:70, 50:140] = (0,0,0)
cv2.imshow("Image", image)
cv2.waitKey(0)