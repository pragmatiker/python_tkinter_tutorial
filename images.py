#!/usr/bin/env python3
import os
import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to use images')
p1 = PhotoImage(file=os.path.join(sys.path[0],'vlc-48.png'))
root.iconphoto(False,p1)

root.mainloop()

