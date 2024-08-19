import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [2, 3, 5, 10])

# plt.plot([2, 3, 5, 10])
# plt.plot(np.array([2, 3, 5, 10]))
# plt.show()

data_dict = {'data_x':[1,2,3,4,5], 'data_y':[2,3,5,10,8]}

plt.plot('data_x', 'data_y', data=data_dict) #put the data_dict to data parameter
plt.show()