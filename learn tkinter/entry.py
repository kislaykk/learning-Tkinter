from tkinter import *

root=Tk()
#entry field
e=Entry(root,width=30,bg="yellow",fg="blue")
e.pack()
e.insert(0,"Enter Your name:")

def myClick():
    hello="hello "+e.get()
    mylabel=Label(root,text=hello,fg="orange")#e.get(),gets the text inside entry field
    mylabel.pack()

#myButton=Button(root,text="click me",state="disabled")
#myButton=Button(root,text="click me",padx=50)
#myButton=Button(root,text="click me",padx=50,pady=50)
myButton=Button(root,text="Enter your name",command=myClick,fg="white",bg="#ff0033")
myButton.pack()

root.mainloop()