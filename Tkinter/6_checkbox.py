from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가


chkvar = IntVar()
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

bt7 = Button(root, text = "click", command = btncmd)
bt7.pack()

root.mainloop()
