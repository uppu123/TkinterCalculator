#step 1: Importing tkinter
import tkinter as tk
from tkinter import ttk

#step 2: Gui Interaction

window = tk.Tk()
window.title("Calculator")
window.geometry('500x500')

#step 3:Adding Inputs

#Entry
e = ttk.Entry(window, width = 56)
e.place(x = 0, y = 0)

#Buttons


#numbers
def click(num):
    result = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(result) + str(num))

b1 = ttk.Button(window, text = '1', width = 12, command = lambda: click(1))
b1.place(x = 10, y = 60)

b2 = ttk.Button(window, text = '2', width = 12, command = lambda: click(2))
b2.place(x = 80, y = 60)

b3 = ttk.Button(window, text = '3', width = 12, command = lambda: click(3))
b3.place(x = 150, y = 60)

b4 = ttk.Button(window, text = '4', width = 12, command = lambda: click(4))
b4.place(x = 10, y = 120)

b5 = ttk.Button(window, text = '5', width = 12, command = lambda: click(5))
b5.place(x = 80, y = 120)

b6 = ttk.Button(window, text = '6', width = 12, command = lambda: click(6))
b6.place(x = 150, y = 120)

b7 = ttk.Button(window, text = '7', width = 12, command = lambda: click(7))
b7.place(x = 10, y = 180)

b8 = ttk.Button(window, text = '8', width = 12, command = lambda: click(8))
b8.place(x = 80, y = 180)

b9 = ttk.Button(window, text = '9', width = 12, command = lambda: click(9))
b9.place(x = 150, y = 180)

b0 = ttk.Button(window, text = '0', width = 12, command = lambda: click(0))
b0.place(x = 10, y = 240)

#operators

def add():
    n1 = e.get()
    global s
    s = "addition"
    global i
    i = int(n1)
    e.delete(0, tk.END)

bo1 = ttk.Button(window, text = '+', width = 12, command = add)
bo1.place(x = 80, y = 240)

def sub():
    n1 = e.get()
    global s
    s = "subtraction"
    global i
    i = int(n1)
    e.delete(0, tk.END)

bo2 = ttk.Button(window, text = '-', width = 12, command = sub)
bo2.place(x = 150, y = 240)

def mul():
    n1 = e.get()
    global s
    s = "multiplication"
    global i
    i = int(n1)
    e.delete(0, tk.END)

bo3 = ttk.Button(window, text = 'x', width = 12, command = mul)
bo3.place(x = 10, y = 300)

def div():
    n1 = e.get()
    global s
    s = "division"
    global i
    i = int(n1)
    e.delete(0, tk.END)

bo4 = ttk.Button(window, text = '/', width = 12, command = div)
bo4.place(x = 80, y = 300)

#Equal To

def equal():
    n2 = e.get()
    e.delete(0, tk.END)
    if s == "addition":
        e.insert(0, i + int(n2))
    elif s == "subtraction":
        e.insert(0, i - int(n2))
    elif s == "multiplication":
        e.insert(0, i * int(n2))
    else:
        if int(n2) == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, i / int(n2))

bequal = ttk.Button(window, text = '=', width = 12, command = equal)
bequal.place(x = 150, y = 300)

#Clear
def clear():
    e.delete(0, tk.END)

bclear = ttk.Button(window, text = 'Clear', width = 12, command = clear)
bclear.place(x = 10, y = 360)

#step 4: mainloop
window.mainloop()

