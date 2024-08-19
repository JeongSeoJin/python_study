import matplotlib.pyplot as plt
import numpy as np

#print(plt.style.available) #사용할 수 있는 종류의 스타일 출력
plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes - width, py_dev_y, color = '#5a7d9a', 
         linewidth = 2, width = width, label = 'Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes, js_dev_y, color = '#adad3b', 
         linewidth = 2, width = width, label = 'JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


plt.bar(x_indexes + width, dev_y, color = '#444444', linestyle = '--', 
         linewidth = 2, width = width, label = 'All Devs') 
# Marker Style can be found in matdplotlib website

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) bu age')

plt.legend(['Python', 'JavaScript', 'All Devs']) # --> legend는 label기능과 동일

plt.xticks(ticks = x_indexes, label = ages_x)
#plt.grid(True) #fivethirtyeight 스타일에는 그리드 기본 설정

plt.tight_layout()

#plt.savefig('plot.png') 현재 디렉토리에 저장

plt.show()