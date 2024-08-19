import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #indeterminate : 작업이 언제 끝날지 모름
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length =150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progressbar의 값을 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text = "start", command = btncmd2)
btn.pack()

root.mainloop()