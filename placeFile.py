from tkinter import *
from tkinter import ttk

root= Tk()
root.geometry('300x300')

userNameFrame= ttk.Frame(root, padding=(5,5))
userNameFrame.pack()


passwordFrame= ttk.Frame(root, padding=(5,5))
passwordFrame.pack()

btnFrame= ttk.Frame(root, padding=(5,2))
btnFrame.pack()

userName_label = ttk.Label(userNameFrame, text="Name: ")
userName_label.pack(side= 'left')

userNameEntry= ttk.Entry(userNameFrame)
userNameEntry.pack()

password_label = ttk.Label(passwordFrame, text="Email: ")
password_label.pack(side= 'left')

passwordEntry= ttk.Entry(passwordFrame)
passwordEntry.pack()

btn= ttk.Button (btnFrame, text= 'Login' )
btn.pack()

root.mainloop()