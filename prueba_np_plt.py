import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,6])
y = np.pow(x,2)

fig, ax = plt.subplots()

ax.plot(x,y)

plt.show()