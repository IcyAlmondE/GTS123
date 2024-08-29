import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3*np.pi, 3*np.pi+0.1, 0.1)
f1 = np.sin(x)
f2 = np.sin(x + 0.5)
f3 = np.sin(x + 1)
f4 = np.sin(x + 1.5)

plt.plot(x, f1, color="blue", linestyle="dotted")
plt.plot(x, f2, color="green", linestyle="dashed")
plt.plot(x, f3, color="orange", linestyle="dashdot")
plt.plot(x, f4, color="pink")

plt.show()