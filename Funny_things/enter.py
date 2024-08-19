x = 5
y = 10
x, y = y, x
print(x)
print(y)

x = (i for i in range(3))
for i in x:
    print(i)

k = list(x for x in range(10))
print(k)

x, y, z = input("enter : ").split()
print(":D : " + x)
print("=] : " + y)
print("X_X : " + z)

s = list(map(int, input().split()))
print(sum(s))