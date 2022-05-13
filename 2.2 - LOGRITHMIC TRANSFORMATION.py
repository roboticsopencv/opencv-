# LOGRITHMIC TRANSFORMATION

import cv2
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

# Read an image
image = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic2.jfif")

# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)

# Display both images
image_file_name = "Original"
plt.title(image_file_name)
plt.imshow(image)
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
image_file_name = "Log Transformed"
plt.title(image_file_name)
plt.imshow(log_image)
plt.show()