from matplotlib import pyplot as plt
import numpy as np
import csv

month =[[],[],[],[],[],[],[],[],[],[],[],[]]

f = open('seoul.csv','r',encoding='cp949')
data =csv.reader(f)
header=next(data)
print(header)
for row in data:
   if row[-1] !='':
      month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.boxplot(month)
plt.show()

f.close()