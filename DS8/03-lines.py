import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 10, 30)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)

