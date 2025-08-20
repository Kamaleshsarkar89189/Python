import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 25, 200)
y1 = 20 - x
y2 = (30 - 2*x) / 3
y1_pos = np.maximum(y1, 0)
y2_pos = np.maximum(y2, 0)
plt.figure(figsize=(7,7))
plt.plot(x, y1_pos, label=r'$x + y = 20$')
plt.plot(x, y2_pos, label=r'$2x + 3y = 30$')
y_region = np.maximum(y1, y2)
plt.fill_between(x, y_region, 25, where=(y_region <= 25), color='lightgreen', alpha=0.5)
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Graphical Solution of LPP')
plt.show()
