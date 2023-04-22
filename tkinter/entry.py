#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.configure('new.TButton')
style.map('new.TButton',
          foreground = [('pressed','green'),('disabled', 'yellow')],
          background = [('pressed','red'),('disabled', 'blue')])

e = ttk.Entry(root,width=50,foreground='green')
e.pack()
e.insert(0,"Enter your Name")
e.focus()

def myClick():
    hello = "Hello " + e.get()
    myLabel = ttk.Label(root, text=hello, background='green', justify='left')
    myLabel.pack()

myButton = ttk.Button(root, text="Print greeting",padding=(5,5),command=myClick, style='new.TButton')
myButton.pack()

root.mainloop()
