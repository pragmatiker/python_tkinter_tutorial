#!/usr/bin/env python3
from tkinter import *

root = Tk()
id_x = 1

def do_some():
    global id_x
    if id_x == 1:
        myLabel.config(background="orange")
    if id_x == 2:
        myLabel.config(background="red")        
    if id_x == 3:
        myLabel.config(background="lightblue")
        root.config(bg="green")
    if id_x == 4:
        myLabel.config(background="blue")
    if id_x == 5:
        myLabel.config(background="lightgreen")                
    if id_x == 6:
        myLabel.config(background="green")
    if id_x == 6:
        id_x = 1
    else:
        id_x += 1

myLabel = Label(root, text="Hoden" , font=('Helvetica',18))
myLabel.pack(padx=5,pady=5)

myButton = Button(root, text="clik",command=do_some)
myButton.pack(padx=5,pady=5)
root.mainloop()


