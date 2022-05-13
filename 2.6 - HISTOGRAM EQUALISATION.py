# HISTOGRAM EQUALISATION

import cv2
from matplotlib import pyplot as plt
#https://www.cambridgeincolour.com/tutorials/histograms1.htm

src = cv2.imread("C:/Users/19R206/PycharmProjects/pythonProject/Resources/pic6.jfif")
src1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
histr = cv2.calcHist([src],[0],None,[256],[0,256])
dst = cv2.equalizeHist(src1)
plt.plot(histr)
plt.show()
plt.hist(histr)
plt.show()
cv2.imshow('Source image', src)
cv2.imshow('Equalized Image', dst)

cv2.waitKey(0)