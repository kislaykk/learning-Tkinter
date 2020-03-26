from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")
#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def popup():
    response=messagebox.showerror("this is my popup","hello world")
    print(response)

Button(root,text="pop up",command=popup).pack()

root.mainloop()