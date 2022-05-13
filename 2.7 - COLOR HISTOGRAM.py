# COLOR HISTOGRAM

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic7.jfif")
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv2.imshow('Source image', img)
cv2.waitKey(0)