import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.43.1:8080/video')

while(True):
    
    ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('CAMERA MOTO', frame)
    #cv2.imshow('GRAY CAMERA', gray)

    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()