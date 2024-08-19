import matplotlib.pyplot as plt
import numpy as np
import csv

#print(plt.style.available) #사용할 수 있는 종류의 스타일 출력
plt.style.use('fivethirtyeight')
#plt.xkcd() #comic style

with open('C:\\Users\pysuk\\Documents\\Coding\\pythonworkspace\\data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row['LanguagesWorkedWith '])


#plt.xlabel('Ages')
#plt.ylabel('Median Salary (USD)')
#plt.title('Median Salary (USD) bu age')

#plt.legend(['Python', 'JavaScript', 'All Devs']) # --> legend는 label기능과 동일

#plt.xticks(ticks = x_indexes, label = ages_x)
#plt.grid(True) #fivethirtyeight 스타일에는 그리드 기본 설정

#plt.tight_layout()

#plt.savefig('plot.png') 현재 디렉토리에 저장

#plt.show()