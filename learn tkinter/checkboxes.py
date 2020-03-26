from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.geometry("400x400")# call this function immediately after root variable
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")

var=StringVar()
c=Checkbutton(root,text="check1",variable=var,onvalue="checked1",offvalue="unchecked1")
c.pack()
c.deselect()
var2=StringVar()
b=Checkbutton(root,text="check2",variable=var2,onvalue="checked2",offvalue="unchecked2")
b.pack()
b.deselect()

def see():
    print(var.get(),var2.get())
d=Button(root,text="see",command=see)
d.pack()

root.mainloop()