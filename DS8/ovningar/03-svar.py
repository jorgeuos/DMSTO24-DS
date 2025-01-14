import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("fruits.csv")

# Gruppera baserat på kategori
category_data = dataFrame.groupby("Product").sum("Sales")
print(category_data)

# Cirkeldiagram
plt.pie(category_data["Sales"], labels=category_data.index, autopct="%1.1f%%")
plt.title("Fördelning av försäljning per kategori")
plt.show()

# Histogram för kvantitet
plt.hist(dataFrame["Quantity"], bins=10)
plt.title("Fördelning av kvantitet")
plt.xlabel("Kvantitet")
plt.ylabel("Frekvens")
plt.show()

