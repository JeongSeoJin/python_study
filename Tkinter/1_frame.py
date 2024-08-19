from tkinter import *

root = Tk()
root.title("GUI")
# root.geometry("640x480")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표

root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

root.mainloop()
