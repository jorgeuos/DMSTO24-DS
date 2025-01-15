import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 10, 30)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]


plt.title("Titel")

plt.xlabel("X-axel")
plt.ylabel("Y-axel")

# Anpassa färger:
plt.plot(x_vals, y_vals, color="red", linestyle="--")

plt.show()


