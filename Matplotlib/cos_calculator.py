import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(math.degrees((math.acos(((b**2 + c**2 - a**2)/ (2 * b * c))))))