from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

def cwf():
    print("Create new file")

menu = Menu(root)

#File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=cwf)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit Menu
menu.add_cascade(label="Edit")

#language Menu 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Jave")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

#View Menu 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minumap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
