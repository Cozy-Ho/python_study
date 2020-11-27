from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

Label(root, text="select menu").pack()

burger_var = IntVar() # int 형으로 값을 저장
btn_burger1 = Radiobutton(root, text="hamberger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="chicken-hamberger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="cheese-hamberger", value=3, variable=burger_var)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="cock", value="cock", variable=drink_var)
btn_drink2 = Radiobutton(root, text="cidar", value="cidar", variable=drink_var)
btn_drink3 = Radiobutton(root, text="tea", value="tea", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 선택된 항목의 값(value)을 반환
    print(drink_var.get())


btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()