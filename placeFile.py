from tkinter import *
from tkinter import ttk

root= Tk()
root.geometry('250x150')


userName_label = ttk.Label(root, text="Username: ")
userName_label.place(x=20, y=20)

userNameEntry = ttk.Entry(root)
userNameEntry.place(x=80, y=20)

password_label = ttk.Label(root, text="Password: ")
password_label.place(x=20, y=45)  

passwordEntry = ttk.Entry(root)
passwordEntry.place(x=80, y=45)  

btn = ttk.Button(root, text='Login')
btn.place(x=100, y=70)

root.mainloop()