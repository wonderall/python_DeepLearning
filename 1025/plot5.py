import matplotlib.pyplot as plt

import numpy as np

x= np.arange(1,5)

y =x**2

 

plt.plot(x,y, label ='y=x^2')

plt.legend(loc='upper left')

plt.show()