import numpy as np
import math
import matplotlib.pyplot as plt

import library
import library.ch2lib.py as ch2

x0 = 0
x1 = 5


x = np.linspace(x0, x1, 200)
y = abs(x**2 - x*x1 - x*x0 + x0*x1)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.axvline(x0+x1/2, color = 'b', label = 'axvline - full height')

plt.show()


ch2.hello()


