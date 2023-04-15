#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master = parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0,0,500,self.list_height))
        self.canvas.pack(expand=True, fill='both')

        # frame inside canvas that holds the widgets
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both',pady=4, padx=10)

        self.canvas.create_window(
            (0,0),
            window = self.frame,
            anchor='nw',
            width=500,
            height=self.list_height
            )
        
        # events ...
        self.canvas.bind_all('<Button-4>', lambda event: self.canvas.yview_scroll(-1, "units"))
        self.canvas.bind_all('<Button-5>', lambda event: self.canvas.yview_scroll(1, "units"))

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame

# setup
window = tk.Tk()
window.geometry('500x400')
window.title('Me Scroll stuff!')

text_list = [('label','button'),
             ('label1','button2'),
             ('label3','button3'),
             ('label4','button4'),
             ('label5','button5'),
             ('label6','button6'),
             ('label7','button7'),
             ('label8','button8'),
             ('label9','button9'),
             ]
list_frame = ListFrame(window, text_list, 100)


# run
window.mainloop()


 