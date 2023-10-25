import matplotlib.pyplot as plt

import numpy as np

x= np.arange(1,5)

y =x**2

 

plt.plot(x,y)

plt.xlim([0,5])

plt.ylim([0,20])

plt.show()