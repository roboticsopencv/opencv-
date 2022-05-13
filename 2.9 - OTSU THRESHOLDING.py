# OTSU THRESHOLDING

import cv2

image1 = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic9.jpg")
cv2.imshow('Input Image', image1)
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# applying Otsu thresholding
# thresholding
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)

# the window showing output image
cv2.imshow('Otsu Threshold', thresh1)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()