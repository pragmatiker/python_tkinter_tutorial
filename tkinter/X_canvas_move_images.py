#!/usr/bin/env python3
import os
from tkinter import *
#from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')

p1 = PhotoImage(file='/home/therty/git/python/python_tkinter_tutorial/tkinter/vlc-48.png')

w = 800
h = 800
x = w/2 - p1.width()/2
y = h/2 - p1.height()/2

myCanvas = Canvas(root,width=w, height=h, bg="white")
myCanvas.pack(padx=20,pady=20)

# Add Image to Canvas
myImage = myCanvas.create_image(x,y,anchor=NW, image=p1)
myLabel = myCanvas.create_text(x,y,text="hodenmumps")

root.mainloop()


