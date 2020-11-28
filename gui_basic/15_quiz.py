from tkinter import *

root = Tk()
root.title("cozy-ho")
root.geometry("640x480") # 가로 * 세로


menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File")
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

root.mainloop()