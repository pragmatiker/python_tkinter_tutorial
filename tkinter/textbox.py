#!/usr/bin/env python3
from tkinter import *

root = Tk()

# Create Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="more text")

# Shove on Screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)

root.mainloop()


