from tkinter import *

root = Tk()
root.title("Jeong Seo Jin")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode = "Extended", height= 10, yscrollcommand = scrollbar.set)
for i in range(1, 31): # 1~31
    listbox.insert(END, "date" + str(i))
listbox.pack(side = "left")

scrollbar.config(command=listbox.yview)

root.mainloop()
