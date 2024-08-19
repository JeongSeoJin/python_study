from tkinter import *

root = Tk()
root.title("GUI")

listbox = Listbox(root, selectmode="extended", height=0) #selectmode 에서 single과 extended의 2가지 옵션이 있다 | height의 높이는 0일 떄 리스트가 가진 모든 것을 보여줌
listbox.insert(0, "apple") 
listbox.insert(1, "banana")
listbox.insert(2, "watermelon")
listbox.insert(END, "watermelon")
listbox.insert(END, "watermelon")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) #맨 앞의 항목 삭제

    # 갯수 확인
    # print("In the list", listbox.size(), " ")

    # 항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    # 선택된 항목 (위치로 반환) (ex) (1, 2, 3)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.geometry("640x480+100+300") #가로 크기, 세로 크기, x좌표, y좌표
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가

root.mainloop()
