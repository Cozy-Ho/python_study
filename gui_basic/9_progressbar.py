import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로

# progressbar = ttk.Progressbar(root, maximum=100, mod="indeterminate")

# progressbar = ttk.Progressbar(root, maximum=100, mod="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()



# btn = Button(root, text="stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01)
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # gui update

        print(p_var2.get())

btn = Button(root, text="start", command=btncmd2)
btn.pack()

root.mainloop()