from tkinter import *

root = Tk()
root.title("GUI")

tt = Text(root, width=30, height=5)
tt.pack()
tt.insert(END, "Write here")

e = Entry(root, width=30)
e.pack()
e.insert(0, "only one line")

def btncmd():
    #내용 출력
    print(tt.get("1.0", END)) #1 : 라인 첫째 줄 0 : 0번째 위치
    print(e.get())
    #내용 삭제
    tt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

root.mainloop()
