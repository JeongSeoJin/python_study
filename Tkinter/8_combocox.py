import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

values = ["date " + str(i) for i in range(1, 32) ]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("card")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text = "select", command = btncmd)
btn.pack()

root.mainloop()
