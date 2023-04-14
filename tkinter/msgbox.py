#!/usr/bin/env python3
import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

def popup(type):
    if type == "info":
        messagebox.showinfo(message="Ya fakkt app")
    if type == "warn":
        messagebox.showwarning(message="Ya fakkt app")
    if type == "err":
        messagebox.showerror(message="Ya fakkt app")
    if type == "qst":
        response = messagebox.askyesno("Ya fakkt app","kaputt myself")
        Label(root,text=response).pack()
        if response == 1:
            root.destroy()

Button(root,text="I quit i", command=lambda: popup('info')).pack()
Button(root,text="I quit w", command=lambda: popup('warn')).pack()
Button(root,text="I quit s", command=lambda: popup('err')).pack()
Button(root,text="I quit a", command=lambda: popup('qst')).pack()

root.mainloop()


