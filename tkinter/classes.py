#!/usr/bin/env python3
from tkinter import *

root = Tk()
id_x = 1

class Elder:

    def __init__(self, main_window) -> None:
        myFrame = Frame(main_window)
        myFrame.pack()

        self.myButton = Button(main_window, text="Click me!", command=self.clicker)
        self.myButton.pack(pady=20)
    
    def clicker(self):
        print("You clicke me!")

e = Elder(root)

root.mainloop()



