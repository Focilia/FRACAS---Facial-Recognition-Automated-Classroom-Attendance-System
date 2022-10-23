import cv2, os   #libraries to na kailangan OpenCV at sa Os para maaccess mga mga files
import sqlite3   #Library ng database SQLITE3
import datetime  #Para sa date 
import time      #Para sa time
import csv       #Para sa csv(Spreadsheet)
import pandas as pd #Library spreadsheet manipulation para sa python (Gagamitin para sa csv) paggawa ng tables then import to csv
import tkinter as tk #Para tk nalang yung pag call sa tkinter
from tkinter import * #Import all in tkinter

win = tk.Tk()#para magamit yung tkinter
win.title("Enter Subject")#Title ng gui
win.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
win.iconbitmap(r'Fracas_Images/FRACAS.ico')
win.configure(background='#20124d') # Background color (Hexadecimal sya) 
win.geometry("500x130")#Laki ng window x,y sya

enterSubj=Label(win, text="Enter SUBJECT" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
enterSubj.place(x=20, y=30)
Subjin=Entry(win,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))#Dito Mag input ng subject tas igeget sa baba
Subjin.place(x=180, y=30)

def facerecog():
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml') #face cascade nag dedetect ng mukha
    capture = cv2.VideoCapture(0) #Capturer
    recognizer = cv2.face.LBPHFaceRecognizer_create()   #Eto recognizer na gamit LBPH algorithm buit in sa openCV
    recognizer.read("train_data.yml") #Trained data galing dun sa peslak_train code Eto nag kikilala

    def getProfile(info): #Function para maconnect sa database at makuha names/student informations
        conn = sqlite3.connect("PeslakDatabase.db") #Eto yung path ng file ng database variable para maconnect sqlite
        cmd = "SELECT * FROM Students WHERE ID="+str(info)
        cursor = conn.execute(cmd)
        profile = None
        for row in cursor:
    
            profile = row
        return profile
        conn.close()

    conn = sqlite3.connect("PeslakDatabase.db")
    read = pd.read_sql_query("SELECT * from Students", conn)
    conn.close()                                                #Para makuha ng pandas(Library) Yung data sa table ng database
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names) 

    font = cv2.FONT_HERSHEY_TRIPLEX #Eto yung fornt bali apat lang sya.
    color = (255, 0, 0) #color ng font
    stroke = 2 #kapal ng font stroke

    while(True):
    
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            color  = (236, 96, 105) #kulay ng rectangle BGR sya hindi RGB
            stroke = 5 #kapal nga rectangle
            end_cord_width  = x + w
            end_cord_height = y + h
            cv2.rectangle(frame, (x, y), (end_cord_width, end_cord_height), color, stroke)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            profile = getProfile(Id)
            if(conf < 35):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=read.loc[read['ID'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                colorT = (97, 237, 228)#BGR
                stroke2 = 2
                cv2.putText(frame, str(profile[1]), (x-50,y-15), font, 1.5, colorT, stroke2, cv2.LINE_AA)
                
            else:
                #print('SINO KA??!')
                name = 'Sino ka??!!'
                colorTx = (0, 0, 255)
                cv2.putText(frame, name, (x,y), font, 1, colorTx, stroke, cv2.LINE_AA)

        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        cv2.imshow("PESLAKRIKUGNAYS", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('PESLAKRIKUGNAYS',cv2.WND_PROP_VISIBLE) < 1:        
        	break    

    capture.release()
    cv2.destroyAllWindows()
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    subject= (Subjin.get())
    fileName="Attendance\Attendance_"+subject+"_"+date+".csv"
    attendance.to_csv(fileName,index=False)

enter = Button(win, text = " ENTER ", font= 'Arial 16 bold', command = facerecog, bg='#a9a9a9', fg='black')
enter.place(x = 200, y = 80)


win.mainloop()