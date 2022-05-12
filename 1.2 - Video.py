# In this program we are importing the video from file location and displaying it in the required pixel size
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("video1.mp4")
# When we give cv2.VideoCapture(0) then the in built camera will be used

while True:
    success, img = cap.read()
    img = cv2.resize(img,(frameWidth, frameHeight))
    cv2.imshow("Result",img)
    if cv2.waitKey(1) == ord('q'):
        break

print("End of Video")
