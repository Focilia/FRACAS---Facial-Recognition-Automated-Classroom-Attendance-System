import cv2
import sqlite3
import tkinter as tk
from tkinter import *           #libraries ng tkinter
from tkinter import messagebox

win = tk.Tk()#para magamit yung tkinter
win.title("ADD ID AND NAME")#Title ng gui
win.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
win.iconbitmap(r'Fracas_Images/FRACAS.ico')
win.configure(background='#20124d') # Background color (Hexadecimal sya) 
win.geometry("550x200")#Laki ng window x,y sya


#Eto code ng input ID
enterID=Label(win, text="Enter ID" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
enterID.place(x=20, y=30)
IDin=Entry(win,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
IDin.place(x=160, y=30)


#Eto naman sa input Name igeget sya sa baba
enterNAME=Label(win, text="Enter NAME" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
enterNAME.place(x=20, y=90)
NAMEin=Entry(win,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
NAMEin.place(x=160, y=90)

def capture():
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

    id =(IDin.get())#Are ginet yung entry function ng tkinter sa taas
    pangalan = (NAMEin.get())#Are ginet yung entry function ng tkinter sa taas
    insertOrUpdate(id, pangalan)# Function call para makapag input ka ng id at name sa database
    pic_num = 0
    # if (id == str(None)):
    #     messagebox.showinfo( "Add Name", 'Put your name inside a quotation mark like this:\n\t           "Your Name" ')


    
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
        if (pic_num>30): #mag  break sya pag 50 na pic
            break 

        if cv2.waitKey(20) & 0xFF == ord('q'): # Para mag exit yung window
            break    

        if cv2.getWindowProperty("PESLAK_CAPTURER",cv2.WND_PROP_VISIBLE) < 1:        
            break

    capture.release()   #Release para wala na capturer pag pindot mo ng Q
    cv2.destroyAllWindows() #Literal na meaning na yan hahah

def addID():
   msg = messagebox.showinfo( "Add ID", 'Put the middle of student ID number in your ID like this:\n\t\t 2020-00123-ST-0 \n\t        You will put the 123 part.')

def addname():
   msg = messagebox.showinfo( "Add Name", 'Put your name inside a quotation mark like this:\n\t           "Your Name" ')

enter = Button(win, text = " ENTER ", font= 'Arial 16 bold', command = capture, bg='#a9a9a9', fg='black')
enter.place(x = 225, y = 140)




howaddID = Button(win, text = " ? ", font= 'Arial 12 bold', command = addID, bg='#a9a9a9', fg='black')
howaddID.place(x = 475, y = 30)

howaddname = Button(win, text = " ? ", font= 'Arial 12 bold', command = addname, bg='#a9a9a9', fg='black')
howaddname.place(x = 475, y = 90)
# howto = Button(win, text = "?", font= 'Arial 16 bold', bg='#a9a9a9', fg='black')
# howto.place(x = 190, y = 150)
win.mainloop()