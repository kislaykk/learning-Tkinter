from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.geometry("400x400")# call this function immediately after root variable
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")
options=["Monday","Tuesday","wednesday","thursday","friday","saturday","sunday"]
def click():
    print(clicked.get())
clicked=StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options)
drop.pack()
b=Button(root,text="day",command=click).pack()
root.mainloop()