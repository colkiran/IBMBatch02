
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title = "IBM"

lbl = Label(win, text="Welcome to tkinter", fg="blue", font=("Harlow Solid Italic", 36))
lbl.place(x = 60, y = 50)

txtfld = Entry(win, font=("Arial", 22))
txtfld.place(x = 85, y = 100)

btn = Button(win, text="Exit", font=("Arial", 36), command=quit)
btn.place(x = 100, y = 200)

win.geometry("600x500+10+20")
win.mainloop()