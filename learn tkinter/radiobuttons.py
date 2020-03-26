from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")

#r=IntVar() 
#r.set(3)

MODES=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza=StringVar()
pizza.set("Pepperoni")

def clicked():
    
    myLabel=Label(root,text=pizza.get())
    myLabel.pack()  


for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode,command=clicked).pack()


#Radiobutton(root,text="option 1",variable=r,value=1,command=clicked).pack()
#Radiobutton(root,text="option 2",variable=r,value=2,command=clicked).pack()

#myLabel=Label(root,text=pizza.get())
#myLabel.pack()
root.mainloop()