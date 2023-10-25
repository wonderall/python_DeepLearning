import csv
import matplotlib.pyplot as plt
f = open('./seoul.csv','r', encoding='cp949')
data = csv.reader(f)

result =[]
next(data)
for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

plt.hist(result, bins =100, color ='r')
plt.show()