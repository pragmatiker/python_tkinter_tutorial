#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

w = 500
h = 500
x = w/2
y = h/2

myCanvas = Canvas(root,width=w, height=h, bg="white")
myCanvas.pack(pady=20)

# Add Image to Canvas
myImage = myCanvas.create_image(0,0,anchor=NW, image=p1)

root.mainloop()


