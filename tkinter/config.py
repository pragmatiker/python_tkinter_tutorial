#!/usr/bin/env python3
from tkinter import *

root = Tk()
id_x = 1

def do_some():
    global id_x
    if id_x == 1:
        myLabel.configure(background="orange")
    if id_x == 2:
        myLabel.configure(background="red")        
    if id_x == 3:
        myLabel.configure(background="lightblue")
    if id_x == 4:
        myLabel.configure(background="blue")
    if id_x == 5:
        myLabel.configure(background="lightgreen")                
    if id_x == 6:
        myLabel.configure(background="green")
        id_x = 0
    id_x += 1

myLabel = Label(root, text="Hoden" , font=('Helveticy',18))
myLabel.pack(padx=5,pady=5)

myButton = Button(root, text="clik",command=do_some)
myButton.pack(padx=5,pady=5)
root.mainloop()


