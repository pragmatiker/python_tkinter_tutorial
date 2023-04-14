#!/usr/bin/env python3
from tkinter import *
summe = 0

root = Tk()
root.title("Calculator")

e = Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def button_click(number):
    #current = e.get()
    #e.delete(0,END)
    e.insert(len(e.get()),number)

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global summe
    global math
    math = "add"
    summe = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global summe
    global math
    math = "sub"
    summe = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global summe
    global math
    math = "mul"
    summe = int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global summe
    global math
    math = "div"
    summe = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0, summe + int(second_number))
    if math == "sub":
        e.insert(0, summe - int(second_number))
    if math == "mul":
        e.insert(0, summe * int(second_number))
    if math == "div":
        e.insert(0, summe / int(second_number))

button_1 = Button(root,text="1",padx=42,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=42,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=42,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=42,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=42,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=42,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=42,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=42,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=42,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=42,pady=20,command=lambda: button_click(0))
button_add = Button(root,text="+",padx=42,pady=20,command=button_add)
button_equal = Button(root,text="=",padx=92,pady=20,command=button_equal)
button_clear = Button(root,text="Clear",padx=80,pady=20,command=button_clear)
button_sub = Button(root,text="-",padx=43,pady=20,command=button_sub)
button_mul = Button(root,text="*",padx=43,pady=20,command=button_mul)
button_div = Button(root,text="/",padx=43,pady=20,command=button_div)
# Put buttons on Screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)

#myButton = Button(root, text="Print greeting", padx=5,pady=5,command=myClick,fg="black",bg="grey",activebackground="white")

root.mainloop()
