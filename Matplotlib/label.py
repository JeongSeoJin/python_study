import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [2, 3, 5, 10])

# plt.plot([2, 3, 5, 10])
# plt.plot(np.array([2, 3, 5, 10]))
# plt.show()

font1 = {'family': 'serif',\
    'color':'black',
    'weight': 'bold',
    'size': 14}

font2 = {'family': 'fantasy',\
    'color': 'deeppink',
    'weight': 'normal',
    'size': 'xx-large'}


#legent loc = best
        # upper right
        # upper left
        # lower left
        # lower right
        # right
        # center left
        # center right
        # lower center
        # upper center
        # center
data_dict = {'data_x':[1,2,3,4,5], 'data_y':[2,3,5,10,8]}
data_dict1 = {'data_x':[1,2,3,4,5], 'data_y':[4,5,6,8, 10]}

plt.plot('data_x', 'data_y', data=data_dict, label='Price ($)') #put the data_dict to data parameter
plt.plot('data_x', 'data_y', data=data_dict1, label='Demand (#)') 

plt.xlabel('X-Label', labelpad=7, fontdict=font1, loc = 'right')
plt.ylabel('Y-Label', labelpad=7, fontdict=font1, loc = 'top')


x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)

# plt.xlim([1, 5])
# plt.ylim([0, 20])
## === same thing
# plt.axis([1, 5, 0, 20])
axis_range = plt.axis('on')
print(axis_range)

#axis's  options : 'on' | 'off' | 'equal' | 'scaled' | 'tight' | 'auto' | 'normal' | 'image' | 'square'

# plt.legend(loc = 'upper left') # <<== 0 = 0%,  1 = 100%, 0.92 = 92%
plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = False, shadow=True)
plt.show()