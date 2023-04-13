#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)
#root.geometry("600x400")

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
var = StringVar()

def show():
    global bSelectBackdrop
    myLabel = Label(root, text=var.get()).grid(row=1,column=1,columnspan=3)
    if var.get() == "on":
        bSelectBackdrop = Button(root, text="Select File",state=ACTIVE)
        myLabel = Text(root, height=1, state=NORMAL, relief=SUNKEN, bd=4)
    if var.get() == "off":
        bSelectBackdrop = Button(root, text="Select File",state=DISABLED)
        myLabel = Text(root, height=1, state=DISABLED, background="grey", relief=SUNKEN, bd=2)
    myLabel.grid(row=0,column=1,sticky=NSEW)
    bSelectBackdrop.grid(row=0,column=2,sticky=E)

c = Checkbutton(root, text="Use Backdrop", variable=var, onvalue="on",offvalue="off",command=show)
c.deselect()
c.grid(row=0,column=0,sticky=W)

myLabel = Text(root, height=1, state=DISABLED, background="grey", relief=SUNKEN, bd=2)
myLabel.grid(row=0,column=1)

bSelectBackdrop = Button(root, text="Select File",state=DISABLED)
bSelectBackdrop.grid(row=0,column=2,sticky=E)

root.mainloop()
