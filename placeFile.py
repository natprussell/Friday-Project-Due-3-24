from tkinter import *
from tkinter import ttk

root= Tk()

frame1= ttk.Frame(root, relief= SOLID)
frame1.place()

userName_label = ttk.Label(frame1, text="Name: ")
userName_label.place(x=20, y=20)

userNameEntry = ttk.Entry(frame1)
userNameEntry.place(x=150, y=20)

password_label = ttk.Label(frame1, text="Email: ")
password_label.place(x=20, y=40)  

passwordEntry = ttk.Entry(frame1)
passwordEntry.place(x=150, y=40)  

btn = ttk.Button(frame1, text='Login')
btn.place(x=70, y=100)

root.mainloop()