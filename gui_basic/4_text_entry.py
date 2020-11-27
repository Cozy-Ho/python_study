from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "INPUT TEXT")

e = Entry(root, width=30) # 엔터 불가 입력창
e.pack()
e.insert(0, "JUST ONE LINE")
def btncmd():
    print(txt.get("1.0", END)) # row 1 , col 0 에서 끝까지.
    print(e.get())
    
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()