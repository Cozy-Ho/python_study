from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0) # height=리스트 목록의 뷰 길이 지정 0은 동적길이
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # delete
    # listbox.delete(0)
    
    # count
    # print("At size is..", listbox.size())
    
    # print("1 to 3 item : ", listbox.get(0,2))
    print("selected item : ", listbox.curselection())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()