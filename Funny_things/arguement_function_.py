import numpy as np

k = np.arange(10)
print(k)

#this is argument that are not limited
def sum(*argument):
    print(*argument)

def sug(*args):
    print(*args)

sum("Hello", 12, "sdf")

#this is integer
sum(int(input("enter any integer : "))\
     + int(input("enter any integer : "))\
         +int(input("enter any integer : ")))

#this is string
sug((input("enter any string : ")), \
    (input("enter any string : ")))