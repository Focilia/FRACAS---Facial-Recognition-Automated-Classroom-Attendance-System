import cv2
import sqlite3
import tkinter as tk
from tkinter import *           #libraries ng tkinter
from tkinter import messagebox

class main:

    def __init__(self,master):
        self.master = master#para magamit yung tkinter
        master.title("ADD ID AND NAME")#Title ng gui
        master.iconbitmap(r'Fracas_Images/FRACAS.ico')
        master.configure(background='#20124d') # Background color (Hexadecimal sya) 
        master.geometry("550x200")#Laki ng window x,y sya
        # Some Usefull variables
        self.ID = StringVar()
        self.addID = StringVar()
        self.addNAMES = StringVar()
        self.addface()

    def addface(self):

        #Eto code ng input ID
        enterID=Label(self.master, text="Enter ID" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
        enterID.place(x=20, y=30)
        IDin=Entry(self.master,textvariable = self.addID ,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        IDin.place(x=160, y=30)


        #Eto naman sa input Name igeget sya sa baba
        enterNAME=Label(self.master, text="Enter NAME" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
        enterNAME.place(x=20, y=90)
        NAMEin=Entry(self.master,textvariable = self.addNAMES ,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        NAMEin.place(x=160, y=90)

        # Nickname=Label(self.master, text="NICKNAME" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
        # Nickname.place(x=20, y=150)
        # NicknameIN=Entry(self.master,textvariable = self.addNickname ,width=30  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        # NicknameIN.place(x=160, y=150)

        enter = Button(self.master, text = " ENTER ", font= 'Arial 16 bold', command = self.capture, bg='#a9a9a9', fg='black')
        enter.place(x = 225, y = 140)




        howaddID = Button(self.master, text = " ? ", font= 'Arial 12 bold', command = self.addID, bg='#a9a9a9', fg='black')
        howaddID.place(x = 475, y = 30)

        howaddname = Button(self.master, text = " ? ", font= 'Arial 12 bold', command = self.addname, bg='#a9a9a9', fg='black')
        howaddname.place(x = 475, y = 90)

        # howaddnickname = Button(self.master, text = " ? ", font= 'Arial 12 bold', command = self.hownickname, bg='#a9a9a9', fg='black')
        # howaddnickname.place(x = 475, y = 150)

    def capture(self):
        mukha_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')#face cascade nag dedetect ng mukha
        capture = cv2.VideoCapture(0)

        def insertOrUpdate(ID, Name):   #Eto function para maconnect sa database SQLITE3
            conn = sqlite3.connect("PeslakDatabase.db")
            cmd = "SELECT * FROM Students WHERE ID=?"
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

        id =(self.addID.get())#Are ginet yung entry function ng tkinter sa taas
        pangalan = (self.addNAMES.get())#Are ginet yung entry function ng tkinter sa taas
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
                cv2.imwrite("Mukha_Dataset/User-"+str(id)+"-"+str(pic_num)+".jpg", gray[y:y+h, x:x+w]) #mag write ng img 
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

    def addID(self):
       msg = messagebox.showinfo( "Add ID", 'Put the middle of student ID number in your ID like this:\n\t\t 2020-00123-ST-0 \n\t        You will put the 123 part.')

    def addname(self):
       msg = messagebox.showinfo( "Full Name", 'Put your full name on the space provided')

    # def hownickname(self):
    #    msg = messagebox.showinfo( "Add NickName", 'Put your nickname on the space provided')


root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()