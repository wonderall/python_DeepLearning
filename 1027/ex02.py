from matplotlib import pyplot as plt
import numpy as np
import csv

aug =[]
jan =[]

f = open('temp.csv','r',encoding='cp949')
data =csv.reader(f)
header=next(data)
print(header)
for row in data:
    month= row[2].split('-')[1]
    print(month)
    if row[-1] !='':
        if month == '08':
            aug.append(float(row[3]))
        elif month == '01':
            jan.append(float(row[3]))
plt.boxplot(aug)
plt.boxplot(jan)
plt.show()

f.close()