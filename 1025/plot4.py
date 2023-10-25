from matplotlib import pyplot as plt
import numpy as np

x= np.arange(1,5)

y = np.arange(2,6)

plt.plot(x,y)

plt.xlabel('X', fontsize =14, labelpad =20)

plt.ylabel('Y', fontsize =20, labelpad =10)

plt.show()
