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
	
def instruction():
	os.startfile("Instruction.txt")

def darkmode():
	win.configure(background='#20124d')

	title = PhotoImage(file= "Fracas_Images/fracasm.png")
	titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

	a = Button(win, image= title,bg='#20124d', border= 0,activebackground='#20124d',command= lightmode)	
	a.place(x = 195,y = 80)
	b = Button(win, image= titlem,bg='#20124d', border= 0,activebackground='#20124d')	
	b.place(x = 110,y = 180)

	A = Button(win, image= addface, command = Mukhacapture, bg='#20124d', border= 0,activebackground='#20124d')	
	A.place(x = 80,y = 250)#pwesto ng button

	B = Button(win, image = trainrec, command = train,  bg='#20124d', border= 0,activebackground='#20124d')#Mga Buttons para macall yung mga functions sa taas
	B.place(x = 270,y = 250)

	C = Button(win, image =autoatten, command = recognize,  bg='#20124d', border= 0,activebackground='#20124d')
	C.place(x = 460,y = 250)

	G = Button(win, image = attenlog, command = attendance_natin,  bg='#20124d', border= 0,activebackground='#20124d')
	G.place(x = 460,y = 363)

	H = Button(win, image = testcam1, command = test_cam,  bg='#20124d', border= 0,activebackground='#20124d')
	H.place(x = 95, y = 363)
	win.mainloop()

def lightmode():
	win.configure(background='#c27ba0')

	LMaddphoto5 = PhotoImage(file= "Fracas_Images/LMFRACAS1.png")
	LMaddphoto6 = PhotoImage(file= "Fracas_Images/LMfracas.png")

	a = Button(win, image= LMaddphoto5,bg='#c27ba0', border= 0,activebackground='#c27ba0', command= darkmode)	
	a.place(x = 195,y = 80)
	b = Button(win, image= LMaddphoto6,bg='#c27ba0', border= 0,activebackground='#c27ba0')	
	b.place(x = 110,y = 180)

	addface = PhotoImage(file= "Fracas_Images/LMaddfn.png")
	trainrec = PhotoImage(file= "Fracas_Images/LMtr.png")
	autoatten = PhotoImage(file= "Fracas_Images/LMautoatten.png")
	attenlog = PhotoImage(file= "Fracas_Images/LMattenlog.png")
	testcam1 = PhotoImage(file= "Fracas_Images/LMtestcam.png")

	A = Button(win, image= addface, command = Mukhacapture, bg='#c27ba0', border= 0,activebackground='#c27ba0')	
	A.place(x = 80,y = 250)#pwesto ng button

	B = Button(win, image = trainrec, command = train,  bg='#c27ba0', border= 0,activebackground='#c27ba0')#Mga Buttons para macall yung mga functions sa taas
	B.place(x = 270,y = 250)

	C = Button(win, image =autoatten, command = recognize,  bg='#c27ba0', border= 0,activebackground='#c27ba0')
	C.place(x = 460,y = 250)

	G = Button(win, image = attenlog, command = attendance_natin,  bg='#c27ba0', border= 0,activebackground='#c27ba0')
	G.place(x = 460,y = 363)

	H = Button(win, image = testcam1, command = test_cam,  bg='#c27ba0', border= 0,activebackground='#c27ba0')
	H.place(x = 95, y = 363)

	win.mainloop()

title = PhotoImage(file= "Fracas_Images/fracasm.png")
titlem = PhotoImage(file= "Fracas_Images/FRACAS.png")

a = Button(win, image= title,bg='#20124d', border= 0,activebackground='#20124d', command= lightmode)	
a.place(x = 195,y = 80)
b = Button(win, image= titlem,bg='#20124d', border= 0,activebackground='#20124d')	
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
menubar.add_cascade(label ='Help', menu= submenu)
submenu.add_command(label = 'Instruction', command= instruction)
submenu.add_command(label = 'About us')

addface = PhotoImage(file= "Fracas_Images/addfn.png")
trainrec = PhotoImage(file= "Fracas_Images/trainrecog.png")
autoatten = PhotoImage(file= "Fracas_Images/autoatten.png")
attenlog = PhotoImage(file= "Fracas_Images/attenlog.png")
testcam1 = PhotoImage(file= "Fracas_Images/testcam.png")


A = Button(win, image= addface, command = Mukhacapture, bg='#20124d', border= 0,activebackground='#20124d')	
A.place(x = 80,y = 250)#pwesto ng button

B = Button(win, image = trainrec, command = train,  bg='#20124d', border= 0,activebackground='#20124d')#Mga Buttons para macall yung mga functions sa taas
B.place(x = 270,y = 250)

C = Button(win, image =autoatten, command = recognize,  bg='#20124d', border= 0,activebackground='#20124d')
C.place(x = 460,y = 250)

G = Button(win, image = attenlog, command = attendance_natin,  bg='#20124d', border= 0,activebackground='#20124d')
G.place(x = 460,y = 363)

H = Button(win, image = testcam1, command = test_cam,  bg='#20124d', border= 0,activebackground='#20124d')
H.place(x = 95, y = 363)



win.mainloop()#loop para manatiling bukas at magshow ang window
			  #Kailangan!!!