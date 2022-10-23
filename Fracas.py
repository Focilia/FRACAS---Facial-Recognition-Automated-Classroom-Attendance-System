import sys #Self explainatory
import os #Self explainatory
import tkinter as tk 
from tkinter import *           #libraries ng tkinter
from tkinter import messagebox as ms
import cv2   #libraries to na kailangan OpenCV at sa Os para maaccess mga mga files
import sqlite3   #Library ng database SQLITE3
import datetime  #Para sa date 
import time      #Para sa time
import csv       #Para sa csv(Spreadsheet)
import pandas as pd #Library spreadsheet manipulation para sa python (Gagamitin para sa csv) paggawa ng tables then import to csv
import numpy as np #numpy lib para conversion ng img sa int
from PIL import Image # Pillow lib para sa img manipulation
import webbrowser as web #Self explainatory

with sqlite3.connect('PeslakDatabase.db') as db:
    cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Administrators (ID TEXT NOT NULL ,PASS TEXT NOT NULL);')
db.commit()
db.close()

#OOP tayo ngayon hahaha anghirap
class main:
    def __init__(self,master):
        
        self.master = master
        master.title("Login/Register")
        master.iconbitmap(r'Fracas_Images/FRACAS.ico')
        master.configure(background='#c4dcdf')
        master.resizable(0, 0)
        master.geometry("650x300")
        
        self.IDins = StringVar()
        self.PASSins = StringVar()
        self.REGIDins = StringVar()
        self.REGPASSins = StringVar()
        
        self.window()

    # Eto Login Function para sa database at malaman ng login form kung may acc o wala
    def login(self):
        #ara makaconnect sa db
        with sqlite3.connect('PeslakDatabase.db') as db:
            c = db.cursor()

        #eto mag find sa database kung may acc na if wala sya mag show sya ng error
        find_user = ('SELECT * FROM Administrators WHERE ID = ? and PASS = ?')
        c.execute(find_user,[(self.IDin.get()),(self.PASSin.get())])
        result = c.fetchall()
        if result:
            self.master.destroy()
            self.AdminFRACAS()
        else:
            ms.showerror('Invalid','Admin Not Found.')
    
    def logins(self):
        #ara makaconnect sa db
        with sqlite3.connect('PeslakDatabase.db') as db:
            c = db.cursor()

        #eto mag find sa database kung may acc na if wala sya mag show sya ng error
        find_user = ('SELECT * FROM Administrators WHERE ID = ? and PASS = ?')
        c.execute(find_user,[(self.IDin.get()),(self.PASSin.get())])
        result = c.fetchall()
        if result:
            self.master.destroy()
            self.AdminFRACAS()
            

        else:
            ms.showerror('Invalid','Admin Not Found.')    

    def new_user(self):
        #Connect sa database
        with sqlite3.connect('PeslakDatabase.db') as db:
            c = db.cursor()

        #Tingin sa db kung may acc na ganun pag wala create sya hahaha
        find_user = ('SELECT * FROM Administrators WHERE ID = ?')
        c.execute(find_user,[(self.REGIDin.get())])        
        if c.fetchall():
            ms.showerror('Error','It is Already Taken Try a Diffrent One.')
        else:
            ms.showinfo('Account Created','Success.')
            self.log()
        #eto yung mag create sa acc iinsert nya sa db 
        insert = 'INSERT INTO Administrators(ID,PASS) VALUES(?,?)'
        c.execute(insert,[(self.REGIDin.get()),(self.REGPASSin.get())])
        db.commit()

        
        #Bali lahat ng nasa baba eh UI ng Login at regform medyo hawig sa css hahahah
    def log(self):
        self.IDins.set('')
        self.PASSins.set('')
        self.head['text'] = 'LOGIN'
        
        self.enterID = Label(self.master,text="Enter ID" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') )
        self.enterID.place(x=30, y=90)
        self.IDin = Entry(self.master,textvariable = self.IDins,width=40 ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        self.IDin.place(x=220, y=90)

        self.enterPASS = Label(self.master,text="Enter PASSWORD" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold '))
        self.enterPASS.place(x=30, y=140)
        self.PASSin = Entry(self.master,textvariable = self.PASSins,width=40  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '), show = "*")
        self.PASSin.place(x=220, y=140)

        self.login = Button(self.master,text = " LOGIN ", font= 'Arial 16 bold', bg='#a9a9a9', fg='black',command= self.logins)
        self.login.place(x = 280, y = 200)

        self.register = Button(self.master,text = " REGISTER ", font= 'Arial 13', bg='#a9a9a9', fg='black',command=self.cr)
        self.register.place(x = 30, y = 250)

        self.CasUser = Button(self.master, text = " CONTINUE AS USER ", font= 'Arial 13', bg='#a9a9a9', fg='black', command = self.ConUser )
        self.CasUser.place(x = 445, y = 250)


        self.REGenterID.place(x=30, y=350)
        self.REGIDin.place(x=220, y=350)
        self.REGenterPASS.place(x=30, y=350)
        self.REGPASSin.place(x=220, y=350)
        self.REGregister.place(x = 270, y = 350)
        self.Blogin.place(x = 30, y = 350)

        
        
    def cr(self):
        self.REGIDins.set('')
        self.REGPASSins.set('')
        self.head['text'] = 'Create Account'

        self.REGenterID=Label(self.master,text="ID NUMBER" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') )
        self.REGenterID.place(x=30, y=90)
        self.REGIDin=Entry(self.master,textvariable = self.REGIDins, width=40 ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        self.REGIDin.place(x=220, y=90)

        self.REGenterPASS=Label(self.master, text="PASSWORD" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold '))
        self.REGenterPASS.place(x=30, y=140)
        self.REGPASSin=Entry(self.master,textvariable = self.REGPASSins ,width=40  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '), show = "*")
        self.REGPASSin.place(x=220, y=140)

        self.REGregister = Button(self.master,text = " REGISTER ", font= 'Arial 16 bold', bg='#a9a9a9', fg='black', command = self.new_user)
        self.REGregister.place(x = 270, y = 200)

        self.Blogin = Button(self.master,text = "BACK TO LOGIN ", font= 'Arial 13', bg='#a9a9a9', fg='black',command=self.log)
        self.Blogin.place(x = 30, y = 250)

        self.enterID.place(x=30, y= 350)
        self.IDin.place(x=220, y=350)
        self.enterPASS.place(x=30, y=350)
        self.PASSin.place(x=220, y=350)
        self.login.place(x = 280, y = 350)
        self.register.place(x = 30, y = 350)
        
            
    def window(self):
        # LOG = Label(self.master, text="LOGIN" ,fg="black"  ,bg="#c4dcdf" ,font=('times', 40, ' bold ') ) 
        # LOG.place(x=245, y=5)



        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.configure(background='#c4dcdf')
        self.head.pack()
        
        self.enterID = Label(self.master,text="Enter ID" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') )
        self.enterID.place(x=30, y=90)
        self.IDin = Entry(self.master,textvariable = self.IDins,width=40 ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
        self.IDin.place(x=220, y=90)

        self.enterPASS = Label(self.master,text="Enter PASSWORD" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold '))
        self.enterPASS.place(x=30, y=140)
        self.PASSin = Entry(self.master,textvariable = self.PASSins,width=40  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '), show = "*")
        self.PASSin.place(x=220, y=140)

        self.login = Button(self.master,text = " LOGIN ", font= 'Arial 16 bold', bg='#a9a9a9', fg='black',command=self.login)
        self.login.place(x = 280, y = 200)

        self.register = Button(self.master,text = " REGISTER ", font= 'Arial 13', bg='#a9a9a9', fg='black',command=self.cr)
        self.register.place(x = 30, y = 250)

        self.CasUser = Button(self.master, text = " CONTINUE AS USER ", font= 'Arial 13', bg='#a9a9a9', fg='black', command = self.ConUser )
        self.CasUser.place(x = 445, y = 250)


    def AdminFRACAS(self):
        win = tk.Tk()#para magamit yung tkinter
        win.title("FRACAS")#Title ng gui
        win.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
        win.iconbitmap(r'Fracas_Images/FRACAS.ico')
        win.configure(background='#c4dcdf') # Background color (Hexadecimal sya) 
        win.geometry("700x500")#Laki ng window x,y sya

        def site():
            web.open("http://127.0.0.1:5500/index.html")

        def Mukhacapture():
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


        def train():                            #Functions para maopen yung mga code
            recognizer = cv2.face.LBPHFaceRecognizer_create()#Built in recognizer ng opencv LBPH algo sya
            path = 'Mukha_Dataset'#path ng images ng faces

            def getImageWithID(path):#Function para makuha image at id na nakalagay sa pangalan ng image
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                faces = []#Empty dictionary para sa faces
                IDs = []#Empty dictionary para sa faces
                for imagePath in imagePaths:#for loop hanngang ma read lahat ng images
                    faceImg = Image.open(imagePath).convert('L')#Mag convert sa grayscale incase na di naka gray image
                    faceNP = np.array(faceImg, "uint8")#Gawin 8bit int yung images
                    ID = int(os.path.split(imagePath)[-1].split('.')[1])#Para makuha ID num na nakalagay sa name ng image
                    faces.append(faceNP)#Append para malagay sa list dun sa empty na dictionary sa taas
                    IDs.append(ID)#Append para malagay sa list dun sa empty na dictionary sa taas
                    cv2.imshow("Nag-eensayoooo...", faceNP)#Pangalang ng win
                    cv2.waitKey(10)

                return IDs, faces

            IDs, faces = getImageWithID(path)
            recognizer.train(faces,np.array(IDs))#Kailangan para ma train recognizer at gawin nnyang data(yml extension sya)
            recognizer.save("train_data.yml")#Eto yung trained data na ireread ng recognizer
            cv2.destroyAllWindows()

        def recognize():
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

        def test_cam():
            cap = cv2.VideoCapture(0)
            # cap1 = cv2.VideoCapture(0)

            while(True):
                
                ret, frame = cap.read()
                # ret, frame1 = cap1.read()
                frame = cv2.flip(frame, 1)
                # frame1 = cv2.flip(frame1, 1)
                # gray  = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)          #LITERAL NA SHOW LANG NG CAMERA TO YAN LANG ANG CODE
                                                                        #Naexplain ko na naman yang mgayan dun sa mga ibang codes
                cv2.imshow('CAMERA MOTO', frame)            
                # cv2.imshow('GRAY CAMERA', gray)

                if cv2.waitKey(20) & 0xFF == ord('q'):                      
                    break
                if cv2.getWindowProperty('CAMERA MOTO',cv2.WND_PROP_VISIBLE) < 1:        
                    break
            cap.release()
            cv2.destroyAllWindows()

        def attendance_natin():
            os.startfile("Attendance")  # Open ng directory ng csv ng attendance

        def exit():
            win.destroy()
            
        def instruction():
            os.startfile("Instruction.txt")

        def database():
            os.startfile("PeslakDatabase.db")

        def imgdata():
            os.startfile("Mukha_Dataset")

        def darkmode():
            win.configure(background='#465461')

            title = PhotoImage(file= "Fracas_Images/fracasm.png")
            titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

            a = Button(win, image= title,bg='#465461', border= 0,activebackground='#465461', command= lightmode)    
            a.place(x = 195,y = 80)
            b = Button(win, image= titlem,bg='#465461', border= 0,activebackground='#465461')   
            b.place(x = 110,y = 180)

            addface = PhotoImage(file= "Fracas_Images/addfn.png")
            trainrec = PhotoImage(file= "Fracas_Images/trainrecog.png")
            autoatten = PhotoImage(file= "Fracas_Images/autoatten.png")
            attenlog = PhotoImage(file= "Fracas_Images/attenlog.png")
            testcam1 = PhotoImage(file= "Fracas_Images/testcam.png")


            A = Button(win, image= addface, command = Mukhacapture, bg='#465461', border= 0,activebackground='#465461') 
            A.place(x = 80,y = 250)#pwesto ng button

            B = Button(win, image = trainrec, command = train,  bg='#465461', border= 0,activebackground='#465461')#Mga Buttons para macall yung mga functions sa taas
            B.place(x = 270,y = 250)

            C = Button(win, image =autoatten, command = recognize,  bg='#465461', border= 0,activebackground='#465461')
            C.place(x = 460,y = 250)

            G = Button(win, image = attenlog, command = attendance_natin,  bg='#465461', border= 0,activebackground='#465461')
            G.place(x = 460,y = 363)

            H = Button(win, image = testcam1, command = test_cam,  bg='#465461', border= 0,activebackground='#465461')
            H.place(x = 95, y = 363)     

            I = Label(win,text="@Melvin Salonga" ,fg="#D1D100"  ,bg="#465461" ,font=('times', 10, ' bold ') )
            I.place(x = 550, y = 450)                            

            win.mainloop()

        def lightmode():
            win.configure(background='#c4dcdf')

            LMaddphoto5 = PhotoImage(file= "Fracas_Images/LMFRACAS1.png")
            LMaddphoto6 = PhotoImage(file= "Fracas_Images/LMfracas.png")

            a = Button(win, image= LMaddphoto5,bg='#c4dcdf', border= 0,activebackground='#c4dcdf', command= darkmode)   
            a.place(x = 195,y = 80)
            b = Button(win, image= LMaddphoto6,bg='#c4dcdf', border= 0,activebackground='#c4dcdf')  
            b.place(x = 110,y = 180)

            addface = PhotoImage(file= "Fracas_Images/LMaddfn.png")
            trainrec = PhotoImage(file= "Fracas_Images/LMtr.png")
            autoatten = PhotoImage(file= "Fracas_Images/LMautoatten.png")
            attenlog = PhotoImage(file= "Fracas_Images/LMattenlog.png")
            testcam1 = PhotoImage(file= "Fracas_Images/LMtestcam.png")

            A = Button(win, image= addface, command = Mukhacapture, bg='#c4dcdf', border= 0,activebackground='#c4dcdf') 
            A.place(x = 80,y = 250)#pwesto ng button

            B = Button(win, image = trainrec, command = train,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')#Mga Buttons para macall yung mga functions sa taas
            B.place(x = 270,y = 250)

            C = Button(win, image =autoatten, command = recognize,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
            C.place(x = 460,y = 250)

            G = Button(win, image = attenlog, command = attendance_natin,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
            G.place(x = 460,y = 363)

            H = Button(win, image = testcam1, command = test_cam,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
            H.place(x = 95, y = 363)

            I = Label(win,text="@Melvin Salonga" ,fg="#191919"  ,bg="#c4dcdf" ,font=('times', 10, ' bold ') )
            I.place(x = 550, y = 450)

            win.mainloop()

        # title = PhotoImage(file= "Fracas_Images/fracasm.png")
        # titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

        # a = Button(win, image= title,bg='#20124d', border= 0,activebackground='#20124d', command= lightmode)  
        # a.place(x = 195,y = 80)
        # b = Button(win, image= titlem,bg='#20124d', border= 0,activebackground='#20124d') 
        # b.place(x = 110,y = 180)

        LMaddphoto5 = PhotoImage(file= "Fracas_Images/LMFRACAS1.png")
        LMaddphoto6 = PhotoImage(file= "Fracas_Images/LMfracas.png")

        a = Button(win, image= LMaddphoto5,bg='#c4dcdf', border= 0,activebackground='#c4dcdf', command= darkmode)   
        a.place(x = 195,y = 80)
        b = Button(win, image= LMaddphoto6,bg='#c4dcdf', border= 0,activebackground='#c4dcdf')  
        b.place(x = 110,y = 180)

        #Eto yung menu bar
        menubar=Menu(win)
        win.configure(menu= menubar)
        #Are naman ang laman sa menubar
        submenu= Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Options', menu= submenu)
        submenu.add_command(label ='Add Face and Name', command = Mukhacapture)
        submenu.add_command(label ='Train Recognizer', command = train)
        submenu.add_command(label ='Auto Attendance',command = recognize )
        submenu.add_command(label ='Attendance Log',command = attendance_natin)
        submenu.add_command(label ='Test Camera', command= test_cam )
        submenu.add_command(label = 'Light Mode', command= lightmode)
        submenu.add_command(label = 'Dark Mode', command= darkmode)
        submenu.add_command(label ='Exit', command= exit)

        submenu= Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Tools', menu= submenu)
        submenu.add_command(label = 'DatabaseSqlite', command= database)
        submenu.add_command(label = 'Image Dataset', command= imgdata)

        submenu= Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Help', menu= submenu)
        submenu.add_command(label = 'Instruction', command= instruction)
        submenu.add_command(label = 'About us', command= site)

        addface = PhotoImage(file= "Fracas_Images/LMaddfn.png")
        trainrec = PhotoImage(file= "Fracas_Images/LMtr.png")
        autoatten = PhotoImage(file= "Fracas_Images/LMautoatten.png")
        attenlog = PhotoImage(file= "Fracas_Images/LMattenlog.png")
        testcam1 = PhotoImage(file= "Fracas_Images/LMtestcam.png")


        A = Button(win, image= addface, command = Mukhacapture, bg='#c4dcdf', border= 0,activebackground='#c4dcdf') 
        A.place(x = 80,y = 250)#pwesto ng button

        B = Button(win, image = trainrec, command = train,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')#Mga Buttons para macall yung mga functions sa taas
        B.place(x = 270,y = 250)

        C = Button(win, image =autoatten, command = recognize,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
        C.place(x = 460,y = 250)

        G = Button(win, image = attenlog, command = attendance_natin,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
        G.place(x = 460,y = 363)

        H = Button(win, image = testcam1, command = test_cam,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
        H.place(x = 95, y = 363)

        I = Label(win,text="@Melvin Salonga" ,fg="#191919"  ,bg="#c4dcdf" ,font=('times', 10, ' bold ') )
        I.place(x = 550, y = 450)                                  



        win.mainloop()#loop para manatiling bukas at magshow ang window
                      #Kailangan!!!

    def ConUser(self):
        self.master.destroy()
        win = tk.Tk()#para magamit yung tkinter
        win.title("FRACAS")#Title ng gui
        win.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
        win.iconbitmap(r'Fracas_Images/FRACAS.ico')
        win.configure(background='#c4dcdf') # Background color (Hexadecimal sya) 
        win.geometry("550x310")#Laki ng window x,y sya

        def site():
            web.open("http://127.0.0.1:5500/index.html")

        def recognize():
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

        def test_cam():
            cap = cv2.VideoCapture(0)
            # cap1 = cv2.VideoCapture(0)

            while(True):
                
                ret, frame = cap.read()
                # ret, frame1 = cap1.read()
                frame = cv2.flip(frame, 1)
                # frame1 = cv2.flip(frame1, 1)
                # gray  = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)          #LITERAL NA SHOW LANG NG CAMERA TO YAN LANG ANG CODE
                                                                        #Naexplain ko na naman yang mgayan dun sa mga ibang codes
                cv2.imshow('CAMERA MOTO', frame)            
                # cv2.imshow('GRAY CAMERA', gray)

                if cv2.waitKey(20) & 0xFF == ord('q'):                      
                    break
                if cv2.getWindowProperty('CAMERA MOTO',cv2.WND_PROP_VISIBLE) < 1:        
                    break
            cap.release()
            cv2.destroyAllWindows()

        def exit():
            win.destroy()
            
        def instruction():
            os.startfile("Instruction.txt")

        def darkmode():
            win.configure(background='#465461')

            title = PhotoImage(file= "Fracas_Images/fracasm.png")
            titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

            a = Button(win, image= title,bg='#465461', border= 0,activebackground='#465461', command= lightmode)    
            a.place(x = 115,y = 30)
            b = Button(win, image= titlem,bg='#465461', border= 0,activebackground='#465461')   
            b.place(x = 30,y = 130)

            
            autoatten = PhotoImage(file= "Fracas_Images/autoatten.png")
            testcam1 = PhotoImage(file= "Fracas_Images/testcam.png")



            C = Button(win, image =autoatten, command = recognize,  bg='#465461', border= 0,activebackground='#465461')
            C.place(x = 280,y = 190)

            H = Button(win, image = testcam1, command = test_cam,  bg='#465461', border= 0,activebackground='#465461')
            H.place(x = 100, y = 190)                               

            win.mainloop()

        def lightmode():
            win.configure(background='#c4dcdf')

            LMaddphoto5 = PhotoImage(file= "Fracas_Images/LMFRACAS1.png")
            LMaddphoto6 = PhotoImage(file= "Fracas_Images/LMfracas.png")

            a = Button(win, image= LMaddphoto5,bg='#c4dcdf', border= 0,activebackground='#c4dcdf', command= darkmode)   
            a.place(x = 115,y = 30)
            b = Button(win, image= LMaddphoto6,bg='#c4dcdf', border= 0,activebackground='#c4dcdf')  
            b.place(x = 30,y = 130)
                
            autoatten = PhotoImage(file= "Fracas_Images/LMautoatten.png")
            testcam1 = PhotoImage(file= "Fracas_Images/LMtestcam.png")


            C = Button(win, image =autoatten, command = recognize,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
            C.place(x = 280,y = 190)

            H = Button(win, image = testcam1, command = test_cam,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
            H.place(x = 100, y = 190)    
            win.mainloop()

        # title = PhotoImage(file= "Fracas_Images/fracasm.png")
        # titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

        # a = Button(win, image= title,bg='#20124d', border= 0,activebackground='#20124d', command= lightmode)  
        # a.place(x = 195,y = 80)
        # b = Button(win, image= titlem,bg='#20124d', border= 0,activebackground='#20124d') 
        # b.place(x = 110,y = 180)

        LMaddphoto5 = PhotoImage(file= "Fracas_Images/LMFRACAS1.png")
        LMaddphoto6 = PhotoImage(file= "Fracas_Images/LMfracas.png")

        a = Button(win, image= LMaddphoto5,bg='#c4dcdf', border= 0,activebackground='#c4dcdf', command= darkmode)   
        a.place(x = 115,y = 30)
        b = Button(win, image= LMaddphoto6,bg='#c4dcdf', border= 0,activebackground='#c4dcdf')  
        b.place(x = 30,y = 130)

        #Eto yung menu bar
        menubar=Menu(win)
        win.configure(menu= menubar)
        #Are naman ang laman sa menubar
        submenu= Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Options', menu= submenu)
        submenu.add_command(label ='Auto Attendance',command = recognize )
        submenu.add_command(label ='Test Camera', command= test_cam )
        submenu.add_command(label = 'Light Mode', command= lightmode)
        submenu.add_command(label = 'Dark Mode', command= darkmode)
        submenu.add_command(label ='Exit', command= exit)


        submenu= Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Help', menu= submenu)
        submenu.add_command(label = 'Instruction', command= instruction)
        submenu.add_command(label = 'About us', command= site)


        autoatten = PhotoImage(file= "Fracas_Images/LMautoatten.png")
        testcam1 = PhotoImage(file= "Fracas_Images/LMtestcam.png")


        C = Button(win, image =autoatten, command = recognize,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
        C.place(x = 280,y = 190)

        H = Button(win, image = testcam1, command = test_cam,  bg='#c4dcdf', border= 0,activebackground='#c4dcdf')
        H.place(x = 100, y = 190)





        win.mainloop()#loop para manatiling bukas at magshow ang window
                      #Kailangan!!!

root = Tk()

main(root)
root.mainloop()

