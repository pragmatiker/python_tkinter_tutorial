#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

myImage = Image.open('/home/therty/Downloads/IMG_20230407_133339090.jpg')
myImage = myImage.resize((800,600))
myImage = myImage.rotate(angle=-90)
myImage = ImageTk.PhotoImage(myImage)
myLabel = Label(image=myImage)
myLabel.pack()

myButton = Button(root,text="I quit", command=root.destroy).pack()

root.mainloop()


