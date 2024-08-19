import numpy as np

def getStatics(*values):
    cnt = 0
    mean = 0
    var = 0
    std = 0
    mean = np.mean(values)
    var = np.var(values)
    std = np.std(values)
    cnt = len(values)

    return cnt, mean, var, std

cnt, mean, var, std = getStatics(1,2,3,4,5)
print("cnt", cnt)
print("mean", mean)
print("var",var)
print("std", std)