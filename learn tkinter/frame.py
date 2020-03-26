from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")

frame=LabelFrame(root,text="this is my frame",padx=50,pady=50)
frame.pack(padx=100,pady=100)

b=Button(frame,text="click")
b2=Button(frame,text="click here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)

root.mainloop()