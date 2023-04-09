#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image
img_idx = 0

def rotate_resize(img_idx):
    global myImage
    myImage = image_list[img_idx]
    myImage = myImage.resize((800,600))
    myImage = myImage.rotate(angle=-90)
    myImage = ImageTk.PhotoImage(myImage)
    return myImage

def next():
    global myLabel
    global img_idx
    global myImage
    global buttonPrev
    global buttonNext
    img_idx = img_idx + 1
    if img_idx == len(image_list)-1:
        buttonNext = Button(root, text=">>",state=DISABLED)
    buttonPrev = Button(root, text="<<",command=prev)
    myLabel.grid_forget()
    buttonPrev.grid(row=1,column=0)
    buttonNext.grid(row=1,column=2)
    myLabel = Label(image=rotate_resize(img_idx)) 
    myLabel.grid(row=0,column=0,columnspan=3)
    return

def prev():
    global myLabel
    global img_idx
    global myImage
    global buttonPrev
    global buttonNext
    img_idx = img_idx - 1
    if img_idx == 0:
        buttonPrev = Button(root, text="<<",state=DISABLED)
    buttonNext = Button(root,text=">>", command=next)
    myLabel.grid_forget()
    buttonPrev.grid(row=1,column=0)
    buttonNext.grid(row=1,column=2)
    myLabel = Label(image=rotate_resize(img_idx)) 
    myLabel.grid(row=0,column=0,columnspan=3)
    return

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

myImg1 = Image.open('/home/therty/Downloads/IMG_20230407_133339090.jpg')
myImg2 = Image.open('/home/therty/Downloads/IMG_20230323_185404756.jpg')
myImg3 = Image.open('/home/therty/Downloads/IMG_20230307_110818890_HDR.jpg')
myImg4 = Image.open('/home/therty/Downloads/PXL_20230408_130459518.jpg')
image_list = [myImg1,myImg2,myImg3,myImg4]


myImage = rotate_resize(img_idx)
myLabel = Label(image=myImage)
myLabel.grid(row=0,column=0,columnspan=3)

buttonPrev = Button(root, text="<<",state=DISABLED)
buttonPrev.grid(row=1,column=0)
buttonExit = Button(root,text="I quit", command=root.destroy)
buttonExit.grid(row=1,column=1)
buttonNext = Button(root,text=">>", command=next)
buttonNext.grid(row=1,column=2)

root.mainloop()


