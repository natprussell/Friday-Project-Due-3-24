from tkinter import *
from tkinter import ttk

root= Tk()
root.geometry ('400x200')

outputFrame= ttk.Frame(root, padding=(5,2))
outputFrame.pack()

firstRowFrame=ttk.Frame(root, padding=(5,0))
firstRowFrame.pack()

secondRowFrame=ttk.Frame(root, padding=(5,0))
secondRowFrame.pack()

thirdRowFrame=ttk.Frame(root, padding=(5,0))
thirdRowFrame.pack()

fourthRowFrame=ttk.Frame(root, padding=(5,0))
fourthRowFrame.pack()

outputEntry= ttk.Entry(outputFrame, state= 'DISABLED', width=40)
outputEntry.pack(side= 'top')

btn7= ttk.Button(firstRowFrame, text= "7")
btn7.pack(side="left")

btn8= ttk.Button(firstRowFrame, text= "8")
btn8.pack(side="left")

btn9= ttk.Button(firstRowFrame, text= "9")
btn9.pack(side="left")

btnDivide= ttk.Button(firstRowFrame, text= "/")
btnDivide.pack(side="left")

btn4= ttk.Button(secondRowFrame, text= "4")
btn4.pack(side="left")

btn5= ttk.Button(secondRowFrame, text= "5")
btn5.pack(side="left")

btn6= ttk.Button(secondRowFrame, text= "6")
btn6.pack(side="left")

btnMulti= ttk.Button(secondRowFrame, text= "X")
btnMulti.pack(side="left")

btn1= ttk.Button(thirdRowFrame, text= "1")
btn1.pack(side="left")

btn2= ttk.Button(thirdRowFrame, text= "2")
btn2.pack(side="left")

btn3= ttk.Button(thirdRowFrame, text= "3")
btn3.pack(side="left")

btnSub= ttk.Button(thirdRowFrame, text= "-")
btnSub.pack(side="left")

btnClear= ttk.Button(fourthRowFrame, text= "C")
btnClear.pack(side="left")

btn0= ttk.Button(fourthRowFrame, text= "0")
btn0.pack(side="left")

btnEqual= ttk.Button(fourthRowFrame, text= "=")
btnEqual.pack(side="left")

btnPlus= ttk.Button(fourthRowFrame, text= "+")
btnPlus.pack(side="left")

root.mainloop()