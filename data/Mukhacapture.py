import cv2
import sqlite3

mukha_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')#face cascade nag dedetect ng mukha
capture = cv2.VideoCapture(0)

def insertOrUpdate(ID, Name):   #Eto function para maconnect sa database SQLITE3
    conn = sqlite3.connect("PeslakDatabase.db")
    cmd = "SELECT * FROM Students WHERE ID="+str(ID)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                     # Baasics to sa sql watch tutrials hahaha
        isRecordExist = 1
    if(isRecordExist==1):
        cmd = "UPDATE Students SET Name="+str(Name)+" WHERE ID="+str(ID)
    else:
        cmd = "INSERT INTO Students(ID, Name) Values("+str(ID)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id = input('Lagay mo kung pang ilan ka: ')
name = input('Type mo pangalan mo: ')
insertOrUpdate(id, name)# Function call para makapag input ka ng id at name sa database
pic_num = 0

while(True):
    
    ret, frame = capture.read() #Para mag read yung capturer sa taas
    frame = cv2.flip(frame, 1)  #mag flif ng camera para mirror sya
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = mukha_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Para gray yung picture

    for (x, y, w, h) in faces:
        pic_num = pic_num+1
        cv2.imwrite("Mukha_Dataset/User."+str(id)+"."+str(pic_num)+".jpg", gray[y:y+h, x:x+w]) #mag write ng img 
        color  = (236, 96, 105) #kulay ng rectangle BGR sya hindi RGB
        stroke = 5 #kapal nga rectangle
        end_cord_width  = x + w #Coordinate ng width
        end_cord_height = y + h  #Coordinate ng height
        cv2.rectangle(frame, (x, y), (end_cord_width, end_cord_height), color, stroke) # Eto yung rectangle
        cv2.waitKey(100)

    cv2.imshow("PESLAK_CAPTURER", frame) #pangalan nung window
    cv2.waitKey(10)
    if (pic_num>50): #mag  break sya pag 50 na pic
        break 

    if cv2.waitKey(20) & 0xFF == ord('q'): # Para mag exit yung window
        break    

capture.release()   #Release para wala na capturer pag pindot mo ng Q
cv2.destroyAllWindows() #Literal na meaning na yan hahah