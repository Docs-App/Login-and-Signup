from tkinter import *
import os
 
creds = 'tempfile.temp'

def Signup():
	global password
	global name
	global scr

	scr = Tk()
	scr.title('Signup')
	instruction = Label(scr, text='Please Enter new Details')
	instruction.grid(row=0, column=0, sticky=E)

	nameL = Label(scr, text='New Username: ')
	pwordL = Label(scr,text='New Password: ')
	nameL.grid(row=1, column=0, sticky=W)
	pwordL.grid(row=2, column=0, sticky=W)

	name = Entry(scr)
	password = Entry(scr, show='*')
	name.grid(row=1, column=1)
	password.grid(row=2, column=1)

	signupButton = Button(scr, text='Signup', command=FSSignup)
	signupButton.grid(columnspan=2, sticky=W)
	scr.mainloop()

def FSSignup():
	with open(creds, 'w') as f:
		f.write(name.get())	
		f.write('\n')
		f.write(password.get())
		f.close()

	scr.destroy()
	Login()

def Login():
	global nameEL
	global pwordEL
	global rootA

	rootA = Tk()
	rootA.title('Login')

	instruction = Label(rootA, text='Please Login\n')
	instruction.grid(sticky=E)

	nameL = Label(rootA, text='Username: ')
	pwordL = Label(rootA, text='Password: ')
	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)

	nameEL = Entry(rootA)
	pwordEL = Entry(rootA, show='*')
	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)

	loginB = Button(rootA, text='Login', command=CheckLogin)
	loginB.grid(columnspan=2, sticky=W)

	rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser)
	rmuser.grid(columnspan=2, sticky=W)
	rootA.mainloop()

def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()

	if nameEL.get() == uname and pwordEL.get() == pword:
		r = Tk()
		r.title('Login  Done')
		r.geometry('200x100')
		rlbl = Label(r, text='\n[+] Logged In')
		rlbl.pack()
		r.mainloop()
	else:
		r = Tk()	
		r.title('Sorry!')
		r.geometry('200x100')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()	

def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

if os.path.isfile(creds):
	Login()
else:
	Signup()
