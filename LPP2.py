import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 25, 200)
y1 = 20 - 0.5*x
y2 = 30 - 1.5*x
y1 = np.maximum(y1, 0)
y2 = np.maximum(y2, 0)
plt.figure(figsize=(7,7))
plt.plot(x, 20 - 0.5*x, label=r'$3x + 2y = 40$')
plt.plot(x, 30 - 1.5*x, label=r'$3x + 2y = 60$')
y_region = np.minimum(20 - 0.5*x, 30 - 1.5*x)
plt.fill_between(x, 0, y_region, where=(y_region >= 0), color='lightgreen', alpha=0.5)
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Graphical Solution of LPP')
plt.show()
