from tkinterdnd2 import *
from tkinter import *

def drop(event):
    global var
    var.set(event.data)

root=TkinterDnD.Tk()
root.title("案件管理")
root.geometry("1500x700")

var=StringVar()
text_box=Entry(root,textvar=var,width=30)
text_box.drop_target_register(DND_FILES)
text_box.dnd_bind("<<Drop>>",drop)
text_box.place(x=485,y=480)

root.mainloop()