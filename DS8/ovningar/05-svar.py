import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("fruits.csv")


# Sammanfattning av datasetet
print(dataFrame.describe())

# Beräkna median och standardavvikelse
print(f"Median för försäljning: {dataFrame['Sales'].median()}")
print(f"Standardavvikelse för försäljning: {dataFrame['Sales'].std()}")

# Identifiera produkter med högst och lägst försäljning
highest_sales = dataFrame.loc[dataFrame["Sales"].idxmax()]
lowest_sales = dataFrame.loc[dataFrame["Sales"].idxmin()]

print("Produkt med högst försäljning:")
print(highest_sales)
print("Produkt med lägst försäljning:")
print(lowest_sales)