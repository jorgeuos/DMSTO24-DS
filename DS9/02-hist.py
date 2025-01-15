import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("../Data-Visualization/Data/titanic_data.csv")

# Testa att vi får något
# print(dataFrame["Age"].head())

plt.hist(dataFrame["Age"].dropna(), bins=8)
plt.title("Fördelning av ålder")
plt.show()
