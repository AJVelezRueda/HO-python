#!/usr/bin/env python
#Ejercicios 7-8
import numpy as np
import matplotlib.pyplot as plt

# generate N random points
x = np.linspace(0, 10, 256, endpoint = True)
y = x**3+x**2-4*x+4

plt.plot(x, y, '-g', label=r'$y = x^3 + x^2-4x + 4$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio')
plt.legend(loc='upper left')

plt.show()
