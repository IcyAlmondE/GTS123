import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 10.1, 0.1)
y = (1+x)/np.sqrt(x)

plt.plot(x, y)
plt.show()