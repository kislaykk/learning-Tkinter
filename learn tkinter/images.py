from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("learn coding by yourself") #adding title
root.iconbitmap("D:\learn tkinter\Icon.ico")

my_img=ImageTk.PhotoImage(Image.open("images\img1.png"))
my_label=Label(image=my_img)
my_label.pack()

button_quit=Button(root,text="exit",command=root.quit)
button_quit.pack()

root.mainloop()