#!/usr/bin/env python3
from tkinter import *

root = Tk()

e = Entry(root,width=50,fg="green",borderwidth=5)
e.pack()
e.insert(0,"Enter your Name")
e.focus()

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Print greeting", padx=5,pady=5,command=myClick,fg="black",bg="grey",activebackground="white")
myButton.pack()

root.mainloop()
