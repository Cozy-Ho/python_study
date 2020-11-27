from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

flag = IntVar()
checkbox = Checkbutton(root, text="Dont show today", variable=flag)
checkbox.select() # 자동 선택 처리
checkbox.deselect() # 선택 해제 처리
checkbox.pack()

flag2 = IntVar()
checkbox2 = Checkbutton(root, text="dont show this week", variable=flag2)
checkbox2.pack()

def btncmd():
    print(flag.get())
    print(flag2.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()