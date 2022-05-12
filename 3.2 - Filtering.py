#FILTERING

import cv2
import numpy as np
image = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic11.jfif")
# Print error message if image is null
if image is None:
    print('Could not read image')
# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [1, 3, 0],
                    [0, 0, 0]])
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()
# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
# Converted to float because we might lose the negative values if kept as input. We can get the exact depth that is specified.
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()

