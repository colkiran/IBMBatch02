
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("IBM")
lbl = Label(win, text="Welcome to TKinter", fg='red', font=("Arial", 22))
lbl.place(x = 60, y = 50)
win.geometry("600x500+10+20")
win.mainloop()
