from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

label = Label(root, text="select menu").pack()

burger_var = IntVar() #여기에 int형으로 값을 저장
btn_burger1 = Radiobutton(root, text="Hambuger", value=1, variable=burger_var) # value 가 숫자면 variable의 상태가 Int으로 적어야함
btn_burger2 = Radiobutton(root, text="Cheezebuger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenbuger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label = Label(root, text="select drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var) # value 가 문자면 variable의 상태가 String으로 적어야함
btn_drink1.select() #기본 값 선택
btn_drink2 = Radiobutton(root, text="cider", value="cider", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음류 중 선택된 라디오 항목의 값(value)을 출력

bt7 = Button(root, text = "order", command = btncmd)
bt7.pack()

root.mainloop()
