from tkinter import *

root = Tk()
root.title("GUI")

root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표

root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

bt1 = Button(root, text = "Button")
bt1.pack()

bt2 = Button(root, padx = 5, pady = 10, text = "Button2323234234234234") #padx, pady 는 글자 값에 따라 변경
bt2.pack()

bt3 = Button(root, padx = 10, pady = 5, text = "Button3")
bt3.pack()

bt4 = Button(root, width = 10, height = 3,text = "Button444444444444444") #width와 height는 고정 값
bt4.pack()

bt5 = Button(root, fg = "red", bg = "Yellow", text = "Hello") 
bt5.pack()

# photo = PhotoImage(file = "GUI/Check.png")
# bt6 = Button(root, image = photo)
# bt6.pack()

def btncmd():
    print("Button have clicked")

bt7 = Button(root, text = "Active button", command = btncmd)
bt7.pack()
root.mainloop()
