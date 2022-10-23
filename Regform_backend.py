from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import sys
import os

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
            os.startfile("FRACAS1.py")

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
            os.startfile("FRACAS1.py")

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

        
        #Bali lahat ng nasa baba eh UI ng Login at regform
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
        

    def ConUser(self):
        self.master.destroy()
        os.startfile("FRACASuser.py")
        
        
    
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


        # self.REGenterID.place(x=30, y=350)
        # self.REGIDin.place(x=220, y=350)
        # self.REGenterPASS.place(x=30, y=350)
        # self.REGPASSin.place(x=220, y=350)
        # self.REGregister.place(x = 270, y = 350)
        # self.Blogin.place(x = 30, y = 350)


        

        


    


root = Tk()

main(root)
root.mainloop()