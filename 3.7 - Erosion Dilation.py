# EROSION DILATION - BINARY IMAGE

import cv2
import numpy as np
def load_img():
    blank_img =np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img
img = load_img()
cv2.imshow("Image", img)
kernel = np.ones((5,5),np.uint8)
erosion1 = cv2.erode(img,kernel,iterations = 4)
cv2.imshow("Eroded Image1", erosion1)

#erosion5 = cv2.erode(img,kernel,iterations = 1)
#cv2.imshow("Eroded Image5", erosion5)

dilation1 = cv2.dilate(img, kernel, iterations=2)
cv2.imshow("Dilated Image", dilation1)

cv2.waitKey(0)