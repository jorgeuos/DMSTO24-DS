import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("fruits.csv")

# Lösning:

# Skapa en ny kolumn för total försäljning
dataFrame["Total_Sales"] = dataFrame["Price"] * dataFrame["Quantity"]

# Filtrera produkter med hög försäljning
top_products = dataFrame[dataFrame["Total_Sales"] > 500]
print(top_products)

# Spara till en ny CSV-fil
# top_products.to_csv("top_products.csv", index=False)

# Skapa ett stapeldiagram
plt.bar(top_products["Product"], top_products["Total_Sales"])

plt.title("Produkter med hög försäljning")
plt.xlabel("Produkt")
plt.ylabel("Total försäljning")
plt.xticks(rotation=45)
plt.show()
