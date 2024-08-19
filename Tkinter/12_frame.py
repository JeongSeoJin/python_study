from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

Label(root, text="choose the Menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

# Menu Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeze burger").pack()
Button(frame_burger, text="chicken burger").pack()

# Drink Frame
frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right",fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sider").pack()

root.mainloop()