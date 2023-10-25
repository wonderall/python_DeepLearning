from matplotlib import pyplot as plt
import numpy as np

image = np.array(([1,0,0.5],
                 [0.1,0.2,0.3],
                 [0.4,0.5,0.6]
                 ))
plt.imshow(image)
plt.show()
