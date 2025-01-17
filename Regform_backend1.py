from tkinter import *
from tkinter import messagebox as ms
import sqlite3

#main Class
class main:

    def __init__(self,master):
        self.master = master
        master.title("Login/Register")
        master.iconbitmap(r'Fracas_Images/FRACAS.ico')
        # Some Usefull variables
        self.ID = StringVar()
        self.PASS = StringVar()
        self.n_ID = StringVar()
        self.n_PASS = StringVar()
        self.window()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('PeslakDatabase.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM Administrators WHERE ID = ? and PASS = ?')
        c.execute(find_user,[(self.ID.get()),(self.PASS.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = 'Logged in as \n' + self.ID.get() 
            self.head['pady'] = 20
        else:
            ms.showerror('Invalid','Admin Not Found.')
            
    def new_user(self):
    	
        with sqlite3.connect('PeslakDatabase.db') as db:
            c = db.cursor()

       
        find_user = ('SELECT * FROM Administrators WHERE ID = ?')
        c.execute(find_user,[(self.ID.get())])        
        if c.fetchall():
            ms.showerror('Error','It is Already Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success','Account Created.')
            self.log()
        
        insert = 'INSERT INTO Administrators(ID,PASS) VALUES(?,?)'
        c.execute(insert,[(self.n_ID.get()),(self.n_PASS.get())])
        db.commit()

        
    def log(self):
        self.ID.set('')
        self.PASS.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_ID.set('')
        self.n_PASS.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def window(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'ID: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.ID,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.PASS,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'ID: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_ID,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_PASS,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

#create window and application object
root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()