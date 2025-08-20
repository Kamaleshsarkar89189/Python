import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 25, 400)
y1 = 10 - x               
y2 = (72 - 3*x) / 4       
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y_region = np.minimum(y1, y2)
plt.figure(figsize=(7, 7))
plt.plot(x, y1, label=r'$2x + 2y = 20$')
plt.plot(x, y2, label=r'$3x + 4y = 72$')
plt.fill_between(x, 0, y_region, where=(y_region >= 0), color='lightgreen', alpha=0.5, label='Feasible Region')
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Graphical Solution of LPP')
plt.show()
