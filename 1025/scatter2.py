from matplotlib import pyplot as plt
import numpy as np

x= np.arange(1,6) #[1,2,3,4,5]
y = x**2

plt.scatter(x,y,marker="D")
plt.show()

