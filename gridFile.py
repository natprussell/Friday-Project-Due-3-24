from tkinter import *
from tkinter import ttk

root= Tk()

frame1= ttk.Frame(root, relief=SOLID, padding=(12,35))
frame1.grid()

name_label = ttk.Label(frame1, text="Name: ")
name_label.grid(row=0, column=0)

nameEntry= ttk.Entry(frame1)
nameEntry.grid(row=0, column=1)

email_label = ttk.Label(frame1, text="Email: ")
email_label.grid(row=1, column=0)

emailEntry= ttk.Entry(frame1)
emailEntry.grid(row=1, column=1)

password_label = ttk.Label(frame1, text="Password: ")
password_label.grid(row=2, column=0)

passwordEntry= ttk.Entry(frame1)
passwordEntry.grid(row=2, column=1)

btn1= ttk.Button(frame1, text= "Sign Up Now")
btn1.grid(row=3, column=1)

root.mainloop()