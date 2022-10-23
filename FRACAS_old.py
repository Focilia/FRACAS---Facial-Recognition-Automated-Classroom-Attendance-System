import sys
import os
import tkinter as tk
from tkinter import *			#libraries ng tkinter
from tkinter import messagebox

win = tk.Tk()#para magamit yung tkinter
win.title("FRACAS")#Title ng gui
win.resizable(0, 0)   #Kung resizable ba o hindi 0= False 1= True
win.iconbitmap(r'FRACAS.ico')
win.configure(background='#20124d') # Background color (Hexadecimal sya) 
win.geometry("700x500")#Laki ng window x,y sya




#ETO naman para maging bacground ang img
#background=PhotoImage(file= "Fracas_Images/background.png")
#background_label = Label(win, image=background)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

title = PhotoImage(file= "Fracas_Images/fracastitle.png")
spacer1 = Label(win, text= " \n \n ", bg= '#20124d' ) # spacer para sa label
label1 = Label(win, image= title, bg= '#20124d')  # ETO YUNG LABEL
spacer2 = Label(win, text= " ", bg= '#20124d' ) # spacer para sa label
label2 = Label(win, text='Facial Recognition Automated Classroom Attendance System',relief= 'solid', font='plasma 15 bold' ,bg='Gray',fg='white')

spacer1.pack()
label1.pack()
spacer2.pack() #Kailangan para sa lumabas Label text
label2.pack()

def Mukhacapture():
	os.system("Mukhacapture.py")

def train():							#Functions para maopen yung mga code
	os.system("Peslak_Train.py")

def recognize():
	os.system("Facerecog-testing.py")

def test_cam():
	os.system("Testing-ng-camera.py")

def attendance_natin():
	os.startfile("C:/Deve/Facerecog/Peslak_sqlite/Attendance")	# Open ng directory ng csv ng attendance

def addname():
   msg = messagebox.showinfo( "Add Name", 'Put your name inside a quotation mark like this:\n\t           "Your Name" ')

def exitcam_recognizer():																								# Button na ? sa GUI
	mes = messagebox.showinfo( "To exit Recog or Cam", "Press Q to exit the Recognizer or the Camera.")

def exit():
	win.destroy()

def changebackground():
	win.configure(background='#f3f3f3')

def instruction():
	os.system("Instruction.txt")

#Eto yung menu bar
menubar=Menu(win)
win.configure(menu= menubar)
#Are naman ang laman sa menubar
submenu= Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Options', menu= submenu)
submenu.add_command(label ='Add Face and Name')
submenu.add_command(label ='Train Recognizer')
submenu.add_command(label ='Auto Attendance')
submenu.add_command(label ='Attendance Log')
submenu.add_command(label ='Test Camera', command= test_cam )
submenu.add_command(label = 'Light Mode', command= changebackground)
submenu.add_command(label ='Exit', command= exit)

submenu= Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu= submenu)
submenu.add_command(label = 'Instruction', command= instruction)
submenu.add_command(label = 'About us')

addphoto = PhotoImage(file= "Fracas_Images/addfn.png")

A = Button(win, image= addphoto, command = Mukhacapture, bg='#20124d', border= 0,activebackground='#20124d')	
A.place(x = 110,y = 220)#pwesto ng button


B = Button(win, text = "Train Recognizer", font= 'Arial 13 bold', command = train, bg='#a9a9a9', fg='black')#Mga Buttons para macall yung mga functions sa taas
B.place(x = 273,y = 220)

C = Button(win, text = "Auto Attendance", font= 'Arial 13 bold', command = recognize, bg='#a9a9a9', fg='black')
C.place(x = 440,y = 220)

D = Button(win, text = " Test  Cam ", font= 'Arial 13 bold', command = test_cam, bg='#a9a9a9', fg='black')
D.place(x = 110, y = 325)

E = Button(win, text = "?", font= 'Arial 13 bold', command = addname, bg='#a9a9a9',  fg='black')
E.place(x = 75,y = 220)
	
F = Button(win, text = "?", font= 'Arial 13 bold', command = exitcam_recognizer, bg='#a9a9a9',  fg='black')
F.place(x = 598,y = 220)

G = Button(win, text = "Attendance \nLog", font= 'Arial 15 bold', command = attendance_natin, bg='#a9a9a9', fg='black')
G.place(x = 453,y = 340)

H = Button(win, text = "Mobile Cam", font= 'Arial 13 bold', command = test_cam, bg='#a9a9a9', fg='black')
H.place(x = 110, y = 363)

I = Button(win, text = " About  Us ", font= 'Arial 13 bold', command = test_cam, bg='#a9a9a9', fg='black')
I.place(x = 110, y = 400)


win.mainloop()#loop para manatiling bukas at magshow ang window
			  #Kailangan!!!