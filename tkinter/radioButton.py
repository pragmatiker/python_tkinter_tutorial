#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

rb1 = IntVar()
rb1.set(1)

def rbSelect(rb1Value):
    rb1Label = Label(rbFrame, text=rb1Value).pack()    

rbFrame = LabelFrame(root,text="your Options",padx=5,pady=5)
rbFrame.pack(padx=5,pady=5)
Radiobutton(rbFrame,text="Option1", variable=rb1, value=1, command=lambda: rbSelect(rb1.get())).pack()
Radiobutton(rbFrame,text="Option2", variable=rb1, value=2, command=lambda: rbSelect(rb1.get())).pack()
Radiobutton(rbFrame,text="Option3", variable=rb1, value=3, command=lambda: rbSelect(rb1.get())).pack()
rb1Label = Label(rbFrame, text=rb1.get()).pack()


root.mainloop()


