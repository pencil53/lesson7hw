import cv2
import numpy as np
import time as t

video = cv2.VideoCapture("Red.mp4")
t.sleep(1)
background = 0
number = 0
for i in range(60):
    checking,background = video.read()
    if checking == False:
        continue
    
background = np.flip(background,axis=1)

while video.isOpened():
    checking2,frame = video.read()
    if not checking2:
        break
    number += 1 
    image = np.flip(frame,axis=1)
    color_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    bottom1 = np.array([100,40,40])
    top1 = np.array([100,255,255])
    firstmask = cv2.inRange(color_image,bottom1,top1)
    bottom2 = np.array([155,40,40])
    top2 = np.array([180,255,255])
    secondmask = cv2.inRange(color_image,bottom2,top2)
    firstmask = firstmask + secondmask
    firstmask = cv2.morphologyEx(firstmask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    firstmask = cv2.dilate(firstmask, np.ones((3,3), np.uint8), iterations = 1)
    secondmask = cv2.bitwise_not(firstmask)
    firstresult = cv2.bitwise_and(background,background,mask= firstmask)
    secondresult = cv2.bitwise_and(image,image,mask= secondmask)
    final_img = cv2.addWeighted(firstresult,1,secondresult,1,0)
    cv2.imshow("red cap",final_img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
cv2.destroyAllWindows()
video.release()