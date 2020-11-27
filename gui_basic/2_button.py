from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

btn1 = Button(root, text="button 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="button 2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button 3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button 4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button 5")
btn5.pack()

def btncmd():
    print("button clicked!!")
    
btn7 = Button(root, text="event button", command=btncmd)
btn7.pack()

root.mainloop()