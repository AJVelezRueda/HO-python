#!/usr/bin/env python
#Ejercicio IV

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame()
df['x'] = [7.5,4.48,8.60,7.73,5.28,4.25,6.99,6.31,9.15,5.06]
df['y'] = [28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89]

plt.scatter(df['x'].tolist(), df['y'].tolist(), alpha=0.5)
plt.ylabel('y')
plt.xlabel('x')
plt.title('Ejercicio 4-6')
plt.show()
