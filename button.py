#!/usr/bin/env python3
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="I got clicked")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=5,pady=5,command=myClick,fg="black",bg="grey",activebackground="white")
myButton.pack()

root.mainloop() 

