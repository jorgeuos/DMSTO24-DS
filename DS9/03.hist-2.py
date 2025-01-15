import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# data = np.random.normal(size=100)
# print(data)

rng = np.random.default_rng()
x = np.arange(0, 15).reshape(3, 5)
print(x)

sns.histplot(x, kde=True)
plt.title("Histogram med täthetskurva")
plt.show()

