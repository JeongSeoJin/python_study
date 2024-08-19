import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4]) #these values in list are y's values # x's values are automatically set to [0, 1, 2, 3]

plt.plot([1,2,3,4], [1,4,9,16], 'ro') # if you do like this, left value will be x's values and right be y's values
plt.axis([0, 6, 0, 20])
plt.show()