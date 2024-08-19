global a
a = 33

def add():
    global a
    a = 34
    b = 4
    return a + b

print(add())
print(a)