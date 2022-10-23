import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap1 = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()
    # ret, frame1 = cap1.read()
    frame = cv2.flip(frame, 1)
    # frame1 = cv2.flip(frame1, 1)
    # gray  = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)			#LITERAL NA SHOW LANG NG CAMERA TO YAN LANG ANG CODE
    														#Naexplain ko na naman yang mgayan dun sa mga ibang codes
    cv2.imshow('CAMERA MOTO', frame)			
    # cv2.imshow('GRAY CAMERA', gray)

    if cv2.waitKey(20) & 0xFF == ord('q'):						
        break
    if cv2.getWindowProperty('CAMERA MOTO',cv2.WND_PROP_VISIBLE) < 1:        
        break
cap.release()
cv2.destroyAllWindows()

