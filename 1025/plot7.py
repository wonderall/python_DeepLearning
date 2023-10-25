import matplotlib.pyplot as plt
import numpy as np

x= np.arange(1,5)

plt.plot(x, x*2,marker='o',color ='y',label ='x=x*2')

plt.plot(x, x+3,marker='s',color ='c',label ='x=x=3')

plt.plot(x, x**2,marker='*',color ='m',label ='x=x**2')

plt.legend()

plt.show()

