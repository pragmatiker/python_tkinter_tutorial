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

org_dim = str(myImage.width) + "x" + str(myImage.height)
print(org_dim)
myImage = myImage.resize((800,600))
myImage = myImage.rotate(angle=-90)
myImage = ImageTk.PhotoImage(myImage)


frame = LabelFrame(root,text=org_dim,padx=5,pady=5) # padding INSIDE frame
frame.pack(padx=10,pady=10) # padding AROUND frame

myImageLabel = Label(frame,image=myImage)
myImageLabel.grid(row=0,column=0,columnspan=2)
myButtonL = Button(frame, text="<- I quit", command=root.destroy)
myButtonL.grid(row=1,column=0)
myButtonR = Button(frame, text="I quit ->", command=root.destroy)
myButtonR.grid(row=1,column=1)

root.mainloop()


