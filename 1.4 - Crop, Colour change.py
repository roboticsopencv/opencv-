import cv2
print("Package Imported")
img = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/Dino.png")
cv2.imshow("Original", img)

(b,g,r) = img[0,0]
print("red: {}, green: {}, blue: {}".format(r,g,b))

img[0,0] = (0,0,255)
(b,g,r) = img[0,0]
print("red: {}, green: {}, blue: {}".format(r,g,b))

corner = img[200:300, 600:800]
# [height, width]
cv2.imshow("Cropped", corner)

img[200:300, 600:800] = (200,50,100)

cv2.imshow("Modified", img)
cv2.imwrite("ColorDino.jpg", img)
cv2.waitKey(0)
