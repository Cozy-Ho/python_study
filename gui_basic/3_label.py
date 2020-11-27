from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text="Hellow world")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="world Hellow")

btn = Button(root, text="Hello world", command=change)
btn.pack()

root.mainloop()