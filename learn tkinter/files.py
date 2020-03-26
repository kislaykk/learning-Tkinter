from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")
def open():
    root.filename=filedialog.askopenfilename(initialdir="D:/learn tkinter/images",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))
    print(root.filename)
my_btn=Button(root,text="open file",command=open).pack()
root.mainloop()