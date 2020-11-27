import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1,32) ]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get())



btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()