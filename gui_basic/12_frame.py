import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

Label(root, text="select menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="hamberger").pack()
Button(frame_burger, text="cheese-hamberger").pack()
Button(frame_burger, text="chicken-hamberger").pack()

frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="cock").pack()
Button(frame_drink, text="cidar").pack()

root.mainloop()