import sys
import os
import tkinter as tk
from tkinter import *			#libraries ng tkinter
from tkinter import messagebox
import webbrowser as web



won = tk.Tk()#para magamit yung tkinter
won.title("Register as Admin")#Title ng gui
won.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
won.iconbitmap(r'Fracas_Images/FRACAS.ico')
won.configure(background='#c4dcdf') # Background color (Hexadecimal sya) 
won.geometry("650x300")#Laki ng window x,y sya

LOG=Label(won, text="Create Account" ,fg="black"  ,bg="#c4dcdf" ,font=('times', 40, ' bold ') ) 
LOG.place(x=170, y=5)

enterID=Label(won, text="ID NUMBER" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
enterID.place(x=30, y=90)
IDin=Entry(won,width=40 ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '))
IDin.place(x=220, y=90)


#Eto naman sa input Name igeget sya sa baba
enterPASS=Label(won, text="PASSWORD" ,fg="yellow"  ,bg="#674ea7" ,font=('times', 15, ' bold ') ) 
enterPASS.place(x=30, y=140)
PASSin=Entry(won,width=40  ,bg="#cccccc" ,fg="black",font=('times', 15, ' bold '), show = "*")
PASSin.place(x=220, y=140)

login = Button(won, text = "BACK TO LOGIN ", font= 'Arial 13', bg='#a9a9a9', fg='black')
login.place(x = 30, y = 250)

register = Button(won, text = " REGISTER ", font= 'Arial 16 bold', bg='#a9a9a9', fg='black')
register.place(x = 270, y = 200)







won.mainloop()





	# username_info = username.get()
	# password_info = password.get()

# 	label(screen1, text = "Please Enter Detail below").pack()
# 	label(screen1, text = "").pack()
# 	label(screen1, text = "Username * ").pack()
# 	username_entry = Entry(screen1, textvariable = username )
# 	username_entry.pack()
# 	label(screen1, text = "password * ").pack()
# 	password_entry = Entry(screen1, textvariable)= password).pack()
#     label(screen1, text = "").pack()
#     button(screen, text = "Register", width = 10, height = 1, command = register_user).pack()

# def log in
#   print("log in session started")

# def main_    
