from cgitb import text
from tkinter import *
import time

root = Tk()
root.title('Digital Clock')
root.geometry('600x250')

def myTime():
    myText = time.strftime("%I:%M:%S %p")
    myText2 = time.strftime("%A\n%B\n%D")
    myLable2.config(text=myText2)
    myLable.config(text=myText)
    myLable.after(1000,myTime)


myLable = Label(root,text="",font=('Arial',72),fg='white',bg='black')
myLable.pack()
myLable2 = Label(root,text="",font=("Arial",24))
myLable2.pack()
myTime()
root.mainloop()
