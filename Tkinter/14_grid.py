from tkinter import *
#GRID
root = Tk()
root.title("Hello")
root.geometry("640x480")

# btn1 = Button(root, text="button 1")
# btn2 = Button(root, text="button 2")

# # btn1.pack()
# # btn2.pack()

# # btn1.pack(side = "left")
# # btn2.pack(side = "right")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

#맨 윗줄
btn16 = Button(root, text = "F16")
btn17 = Button(root, text = "F17")
btn18 = Button(root, text = "F18")
btn19 = Button(root, text = "F19")

btn16.grid(row = 0, column = 0)
btn17.grid(row = 0, column = 1)
btn18.grid(row = 0, column = 2)
btn19.grid(row = 0, column = 3)

#clear line
btin_clear = Button(root, text="clear")
btin_equal = Button(root, text="=")
btin_div = Button(root, text="/")
btin_mul = Button(root, text="*")



root.mainloop()