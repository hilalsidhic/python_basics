from tkinter import *

window=Tk()

window.geometry('300x150')
window.configure(bg="red")

def prnt():
    print("button clicked")

button1=Button(window,text="Click Me",bd='5',bg="blue",command=prnt)
button2=Button(window,text="Click Me",bd='5',bg="blue",command=prnt)

button1.grid(row=0,column=0)
button2.grid(row=3,column=1)


window.mainloop()