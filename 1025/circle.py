from matplotlib import pyplot as plt
import numpy as np


ratio =[20,30,40,60]

label = ['Amy','Betty','Chris','Dorothy']

plt.pie(ratio, labels=label, autopct ="%1.1f%%")

plt.show()