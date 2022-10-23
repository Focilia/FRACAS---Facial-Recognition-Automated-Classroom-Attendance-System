import cv2
import sqlite3

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture('http://192.168.43.1:8080/video')

def insertOrUpdate(ID, Name):
    conn = sqlite3.connect("PeslakDatabase.db")
    cmd = "SELECT * FROM Students WHERE ID="+str(ID)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist==1):
        cmd = "UPDATE Students SET Name="+str(Name)+" WHERE ID="+str(ID)
    else:
        cmd = "INSERT INTO Students(ID, Name) Values("+str(ID)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id = input('Lagay mo kung pang ilan ka: ')
name =  input('Type mo pangalan mo: ')
insertOrUpdate(id, name)
pic_num = 0

while(True):
    
    ret, frame = capture.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        pic_num = pic_num+1
        cv2.imwrite("Mukha_Dataset/User."+str(id)+"."+str(pic_num)+".jpg", gray[y:y+h, x:x+w])
        color  = (0 , 200, 0) #kulay ng rectangle BGR sya hindi RGB
        stroke = 4 #kapal nga rectangle
        end_cord_width  = x + w
        end_cord_height = y + h
        cv2.rectangle(frame, (x, y), (end_cord_width, end_cord_height), color, stroke)
        cv2.waitKey(100)

    cv2.imshow("PESLAK_CAPTURER", frame)
    cv2.waitKey(1)
    if (pic_num>50):
        break 

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

capture.release()
cv2.destroyAllWindows()