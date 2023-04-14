#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
var = StringVar()

def show():
    if var.get() == "on":
        bSelectBackdrop.configure(state=NORMAL)
        myLabel.configure(state=NORMAL)
    if var.get() == "off":
        bSelectBackdrop.configure(state=DISABLED)
        myLabel.configure(state=DISABLED)

c = Checkbutton(root, text="Use Backdrop", variable=var, onvalue="on",offvalue="off",command=show)
c.deselect()
c.grid(row=0,column=0,sticky=W)

myLabel = Text(root, height=1, state=DISABLED, background="grey", relief=SUNKEN, bd=2)
myLabel.grid(row=0,column=1)

bSelectBackdrop = Button(root, text="Select File",state=DISABLED)
bSelectBackdrop.grid(row=0,column=2,sticky=E)

root.mainloop()
