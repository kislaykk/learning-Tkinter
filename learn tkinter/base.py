from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")

def open():
    global my_img
    top=Toplevel()
    top.title("2nd one")
    my_img=ImageTk.PhotoImage(Image.open("images\img1.png"))
    my_label=Label(top,image=my_img).pack()
    btn2=Button(top,text="close",command=top.destroy).pack()

btn=Button(root,text="open second window",command=open).pack()
mainloop()