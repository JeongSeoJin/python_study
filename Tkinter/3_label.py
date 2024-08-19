from tkinter import *

root = Tk()
root.title("GUI")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="GUI/Check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="see you again")
    
    global photo2 #Garbage Collection : 불필요한 메모리 공간 해제 <= 이것을 피하려면 변수를 전역 변수로 만들어 줘야함
    photo2 = PhotoImage(file="GUI/x.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

root.mainloop()
