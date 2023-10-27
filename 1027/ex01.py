from matplotlib import pyplot as plt
import numpy as np
import csv

aug =[]
jan =[]

f = open('seoul.csv','r',encoding='cp949')
data =csv.reader(f)
header=next(data)
print(header)
for row in data:
    month=row[0].split('-')[1]
    if row[-1] !='':
        if month == '08':
            aug.append(float(row[-1]))
        elif month == '01':
            jan.append(float(row[-1]))

plt.hist(aug, bins=100, color='r',label='Aug')
plt.hist(jan, bins=100, color='b',label='Jan')
plt.legend()
plt.show()

f.close()