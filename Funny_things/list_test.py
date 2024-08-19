n_list = [x for x in range(20) if x%2 == 0]
print("✔😉 " + str(n_list))
print(n_list)

#the emotions are shown by 'windows + ;'key

n_list1 = [x for x in range(100)
    if x%2 == 0 and x%5 == 0]

print(n_list1)

## dictionary comprehension
obj = {x:x**2 for x in range(6)}
print(obj)