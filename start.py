#!/usr/bin/python
from Tkinter import *
top=Tk()

# def helloCallBack():
#     os.system('python captureVideo.py')

# B=Tkinter.Button(top,text="Video Capture",command= helloCallBack)
#B.pack()va
var=StringVar()
var2=StringVar()
label=Label(top,textvariable=var,relief=RAISED,width='200',fg='red',bd=0)
var.set("Facial Expression recognition system")
label.config(font=("Comic Sans MS", 44))


label2=Label(top,textvariable=var2,relief=RAISED,width='200',fg='black',justify='left',bd=0)
var2.set("Instructions")
label2.config(font=("Comic Sans MS", 20))

var3=StringVar()
label3=Label(top,textvariable=var3,relief=RAISED,width='200',fg='black',justify='left',bd=0)
var3.set("")


label.pack()
label2.pack()

top.mainloop()