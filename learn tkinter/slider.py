from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.geometry("400x400")# call this function immediately after root variable
root.title("learn coding by yourself") #adding title
root.iconbitmap("Icon.ico")
def slide(var):
    root.geometry(str(horizontal.get())+"x400")
    root.pack()
vertical=Scale(root,from_=0,to=200)#dont pack here
vertical.pack()

horizontal=Scale(root,from_=0,to=200,orient=HORIZONTAL,command=slide)#dont pack here
horizontal.pack()


root.mainloop()