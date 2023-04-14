#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

rbFrame = LabelFrame(root,text="your Options",padx=5,pady=5)
rbFrame.pack(padx=5,pady=5)
rb1Label = Label(rbFrame)

TOPPINGS = [
    ("Peperoni","Peperoni"),
    ("Schinken","Schinken"),
    ("Salami","Salami"),
    ("Käse","Käse"),
    ("Zwiebeln","Zwiebeln"),
]

pizzaTopping = StringVar()
pizzaTopping.set("Peperoni")

def rbSelect(rb1Value):
    rb1Label = Label(rbFrame, text=rb1Value)
    rb1Label.pack()    

for ToppingsText, ToppingsTopping in TOPPINGS:
    Radiobutton(rbFrame,text=ToppingsText, variable=pizzaTopping, value=ToppingsTopping).pack(anchor=W)

myButton = Button(rbFrame,text="selct",command=lambda: rbSelect(pizzaTopping.get())).pack()

root.mainloop()


