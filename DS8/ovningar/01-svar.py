import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("fruits.csv")

# Gruppera och summera försäljning per produkt
grouped_data = dataFrame.groupby("Product").sum("Sales")
print(grouped_data)

# Skapa ett stapeldiagram
plt.bar(grouped_data.index, grouped_data["Sales"])
plt.title("Total försäljning per produkt")
plt.xlabel("Produkt")
plt.ylabel("Försäljning")
plt.show()

# Gruppera och summera försäljning över tid
time_series = dataFrame.groupby("Date").sum("Sales")
plt.plot(time_series.index, time_series["Sales"])
plt.title("Försäljning över tid")
plt.xlabel("Datum")
plt.ylabel("Försäljning")
plt.show()

