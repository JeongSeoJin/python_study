import turtle as t

s = t.Screen()
s.setup(650, 800)
s.bgcolor("lightcyan")


t.color("Black", "#f0a53a")

t.penup()
t.goto(0, 210)
t.pendown()
t.begin_fill()
t.setheading(180)
t.circle(10)
t.end_fill()
t.penup()

t.goto(-10,180)
t.pendown()
t.begin_fill()
t.pendown()
t.goto(-10,0)
t.setheading(90)
t.goto(10, 0)
t.setheading(90)
t.goto(10,180)
t.end_fill()


s.mainloop()