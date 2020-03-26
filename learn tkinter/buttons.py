from tkinter import *

root=Tk()

def myClick():
    mylabel=Label(root,text="Look i clicked a button")
    mylabel.pack()

#myButton=Button(root,text="click me",state="disabled")
#myButton=Button(root,text="click me",padx=50)
#myButton=Button(root,text="click me",padx=50,pady=50)
myButton=Button(root,text="click me",command=myClick,fg="white",bg="#ff0033")
myButton.pack()

root.mainloop()