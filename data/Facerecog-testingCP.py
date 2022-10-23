import cv2, os
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture('http://192.168.43.1:8080/video')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("train_data.yml")

def getProfile(name):
    conn = sqlite3.connect("PeslakDatabase.db")
    cmd = "SELECT * FROM Students WHERE ID="+str(name)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

font = cv2.FONT_HERSHEY_TRIPLEX
color = (255, 0, 0)
stroke = 2

while(True):
    
    ret, frame = capture.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        color  = (0 , 200, 0) #kulay ng rectangle BGR sya hindi RGB
        stroke = 4 #kapal nga rectangle
        end_cord_width  = x + w
        end_cord_height = y + h
        cv2.rectangle(frame, (x, y), (end_cord_width, end_cord_height), color, stroke)
        name, conf = recognizer.predict(gray[y:y+h, x:x+w])
        profile = getProfile(name)
        if(conf<55):
            print(profile)
            colorT = (255, 0 ,0)
            cv2.putText(frame, str(profile[1]), (x,y-10), font, 1.5, colorT, stroke, cv2.LINE_AA)
        
        if (conf>60):
            print('SINO KA??!')
            name = 'SINO KA??!'
            colorTx = (0, 0, 255)
            cv2.putText(frame, name, (x,y), font, 1, colorTx, stroke, cv2.LINE_AA)

    cv2.imshow("PESLAKRIKUGNAYS", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

capture.release()
cv2.destroyAllWindows()